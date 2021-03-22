from uuid import uuid4

def parse(notification):
    return str(notification), uuid4()
