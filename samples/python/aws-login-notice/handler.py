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

def login(event, context):
    logger.info(str(event))
    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': "login"
    }

    req = Request(SLACK_HOOK_URL, json.dumps(slack_message).encode('utf-8'))

    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
