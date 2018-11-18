import boto3
import logging
import os
from lib import slack

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_HOOK_URL = os.environ['SLACK_HOOK_URL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def login(event, context):
    logger.info(str(event))

    detail = event['detail']
    user_identity = detail['userIdentity']
    additonal_event_data = detail['additionalEventData']

    attachments = [
        slack.build_attachment('アカウント', user_identity['arn']),
        slack.build_attachment('ログイン時刻', detail['eventTime']),
        slack.build_attachment('IP', detail['sourceIPAddress']),
        slack.build_attachment('ユーザエージェント', detail['userAgent']),
        slack.build_attachment('MFA利用', additonal_event_data['MFAUsed']),
    ]

    title = 'AWSコンソールログイン通知'

    slack.send(
        SLACK_HOOK_URL,
        SLACK_CHANNEL,
        title,
        attachments
    )
