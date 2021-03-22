import json

def parse(notification):
    message = json.loads(notification)

    status = message['status']

    timestamp = message['notification']['timestamp']

    delivery = message['delivery']
    phone_carrier = delivery.get('phoneCarrier', 'error')
    destination = delivery['destination']
    response = delivery['providerResponse']
    price = delivery['priceInUSD']

    filename = timestamp.replace(' ', 'T') + '_' + status + '_' + destination
    text = (
        '*SMS - {}* @ {}\n\n'
        '*Destination:* {} ({})\n'
        '*Response:* {}\n'
        '*Price:* ${}'
    ).format(status, timestamp, destination, phone_carrier, response, price)

    return text, filename
