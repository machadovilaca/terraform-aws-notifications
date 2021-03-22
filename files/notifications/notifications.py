#!/usr/bin/python3.6
import boto3
import os
import urllib3
import json

from record import record_event_handler
from cw import cw_event_handler


s3_client = boto3.client('s3')
s3_bucket = boto3.resource('s3').Bucket(os.environ['S3_BUCKET_NAME'])

http = urllib3.PoolManager()


def write_to_slack(text):
    payload = '[{"type":"section","text":{"type":"mrkdwn","text":"' + text + '"}},{"type":"divider"}]'

    msg = {
        'channel': os.environ['SLACK_CHANNEL'],
        'username': os.environ['SLACK_USERNAME'],
        'blocks': payload,
        'icon_emoji': ''
    }

    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', os.environ['SLACK_WEBHOOK_URL'], body=encoded_msg)


def write_to_s3(text, s3_path):
    s3_bucket.put_object(Key=s3_path, Body=json.dumps(text))


def write(type, origin, text, s3_path):
    targets = ["S3"]

    cw_log_groups = json.loads(os.environ['CW_LOG_GROUPS'])
    #cw_log_groups = json.loads('{"sns/eu-west-1/237093669542/DirectPublishToPhoneNumber":{"targets":["SLACK","S3"]}}')

    sns_topic_arns = json.loads(os.environ['SNS_TOPIC_ARNS'])
    #sns_topic_arns = json.loads('{"arn:aws:sns:eu-west-1:526266413792:ses_tst_deliveries":{"targets":["SLACK"]}}')

    if type == "CW" and origin in cw_log_groups:
        targets = cw_log_groups[origin]["targets"]
    if type == "SNS" and origin in sns_topic_arns:
        targets = sns_topic_arns[origin]["targets"]

    if "SLACK" in targets:
        #print("SLACK")
        write_to_slack(text)

    if "S3" in targets:
        #print("S3")
        write_to_s3(text, s3_path)

    if "ES" in targets:
        print("ES is not supported yet")

    #print(text)
    #print(s3_path)


# Some notification examples - https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html
def notifications(event, context):
    parsed = ""

    if 'awslogs' in event:
        text, s3_path, origin = cw_event_handler(event)
        parsed = "CW"
    elif 'Records' in event:
        text, s3_path, origin = record_event_handler(event)
        parsed = "SNS"

    if parsed != "":
        write(parsed, origin, text, s3_path)
    else:
        # Maybe should be raw printed to s3?
        print('Unknown event type')
        print(json.dumps(event, indent = 4))


# if __name__ == '__main__':
#     import sys
#     s = open(sys.argv[1], 'r').read()
#     j = json.loads(s)

#     notifications(j, '')
