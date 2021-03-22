import json

def parse(notification):
    subject = notification['Subject']
    timestamp = notification['Timestamp']
    message = json.loads(notification['Message'])

    event_source = message['Event Source']
    event_time = message['Event Time']
    event_message = message['Event Message']

    filename = timestamp + '_' + event_source

    text = (
        '*{}* @ {}\n\n'
        '*Source:* {} at {}\n'
        '*Subject:* {}'
    ).format(subject, timestamp, event_source, event_time, event_message)

    return text, filename
