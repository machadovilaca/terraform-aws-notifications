import gzip
import base64
import json
from formats import generic, sms
from datetime import date
from uuid import uuid4
from io import BytesIO


def parse_cw_event(notification):
    text = ''
    type = 'cw'
    filename = 'cw_log'

    if 'delivery' in notification:
        type = 'sms'
        text, filename = sms.parse(notification)
    else:
        text, filename = generic.parse(notification)

    return text, type, filename


def parse_cw_events(log_events):
    text = ''
    type = 'cw' # Default value
    filename = 'cw_log' # Default value

    for log_event in log_events:
        log_text, type, filename = parse_cw_event(log_event['message'])
        text = text + log_text + '\n'

    return text, type, filename


def cw_event_handler(event):
    cw_data = str(event['awslogs']['data'])
    cw_logs = gzip.GzipFile(fileobj=BytesIO(base64.b64decode(cw_data, validate=True))).read()
    log_events = json.loads(cw_logs)

    origin = log_events['logGroup']

    text, type, filename = parse_cw_events(log_events['logEvents'])

    s3_path = '{}/{}/{}.txt'.format(type, date.today().strftime('%Y%m%d'), filename)

    return text, s3_path, origin
