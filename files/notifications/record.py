import json
from datetime import date
from formats import generic, ses, rds


def parse_from_sns(notification):
    sns = notification["Sns"]
    message = json.loads(sns["Message"])

    if "mail" in message:
        type = "ses"
        text, filename = ses.parse(sns)
    elif "RDS" in notification["Sns"]["Subject"]:
        type = "rds"
        text, filename = rds.parse(sns)
    else:
        type = "sns"
        text, filename = generic.parse(sns)

    return text, type, filename


def parse_from_source(source, notification):
    if source == "aws:sns":
        text, type, filename = parse_from_sns(notification)
    else:
        type = source
        text, filename = generic.parse(notification)

    return text, type, filename


def parse_record_event(record):
    if "EventSource" in record:
        text, type, filename = parse_from_source(record["EventSource"], record)
    elif "eventSource" in record:
        text, type, filename = parse_from_source(record["eventSource"], record)
    else:
        type = "record"
        text, filename = generic.parse(record)

    return text, type, filename


def record_event_handler(notification):
    text = ""
    type = "record" # Default value
    filename = "record_log" # Default value

    for record in notification['Records']:
        origin = record['Sns']['TopicArn']
        log_text, type, filename = parse_record_event(record)
        text = text + log_text + "\n"

    s3_path = "{}/{}/{}.txt".format(type, date.today().strftime("%Y%m%d"), filename)

    return text, s3_path, origin
