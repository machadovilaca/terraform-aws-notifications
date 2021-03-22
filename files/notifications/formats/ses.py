import json

def parse(notification):
    topic = notification['TopicArn'].split(':')[5]

    message = json.loads(notification['Message'])
    source = message['mail']['source']
    source_ip = message['mail']['sourceIp']
    destination = message['mail']['destination']

    delivery = message.get('delivery', {})
    remote_mta_ip = delivery.get('remoteMtaIp', '')

    timestamp = message['mail']['timestamp']
    subject = message['mail']['commonHeaders']['subject']

    filename = timestamp + '_' + destination[0]

    text = (
        '*{}* @ {}\n\n'
        '*Source:* {} ({})\n'
        '*Destination:* {} ({})\n'
        '*Subject:* {}'
    ).format(topic, timestamp, source, source_ip, destination, remote_mta_ip, subject)

    return text, filename
