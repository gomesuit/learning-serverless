import boto3
import json
import logging
import os

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SLACK_HOOK_URL = os.environ['SLACK_HOOK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def send_slack(slack_message):
    req = Request(SLACK_HOOK_URL, json.dumps(slack_message).encode('utf-8'))

    logger.info(json.dumps((slack_message)))
    # return

    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)

def build_attachment(title, value):
    return {
        "fields":[
            {
                "title": title,
                "value": value
            }
        ]
    }

def login(event, context):
    logger.info(str(event))

    detail = event['detail']
    user_identity = detail['userIdentity']
    additonal_event_data = detail['additionalEventData']

    attachments = [
        build_attachment('アカウント', user_identity['arn']),
        build_attachment('ログイン時刻', detail['eventTime']),
        build_attachment('IP', detail['sourceIPAddress']),
        build_attachment('ユーザエージェント', detail['userAgent']),
        build_attachment('MFA利用', additonal_event_data['MFAUsed']),
    ]

    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': 'AWSコンソールログイン通知',
        'attachments': attachments
    }

    send_slack(slack_message)
