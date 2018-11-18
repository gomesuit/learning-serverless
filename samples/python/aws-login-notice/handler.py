import boto3
import logging
import os
import send_slack

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def login(event, context):
    logger.info(str(event))

    detail = event['detail']
    user_identity = detail['userIdentity']
    additonal_event_data = detail['additionalEventData']

    attachments = [
        send_slack.build_attachment('アカウント', user_identity['arn']),
        send_slack.build_attachment('ログイン時刻', detail['eventTime']),
        send_slack.build_attachment('IP', detail['sourceIPAddress']),
        send_slack.build_attachment('ユーザエージェント', detail['userAgent']),
        send_slack.build_attachment('MFA利用', additonal_event_data['MFAUsed']),
    ]

    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': 'AWSコンソールログイン通知',
        'attachments': attachments
    }

    send_slack.send_slack(slack_message)
