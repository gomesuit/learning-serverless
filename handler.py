import json
import os
import requests

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def reply(event, context):
    print event

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    reply_token = json.loads(event['body'])['events'][0]['replyToken']
    text = json.loads(event['body'])['events'][0]['message']['text']
    print reply_token
    print text

    post_text(reply_token, text)

    return response

def post_text(reply_token, text):
    REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % ACCESS_TOKEN
    }

    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
    }

    response = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))
    print response.text
