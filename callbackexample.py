import json
class KafkaProducer:
    def __init__(self, value_serializer):
        self.f= value_serializer

    def send(self, value):
        print(self.f(value))

def my_serializer(v):
    return json.dumps(v).encode('utf-8')


if __name__ == '__main__':
    producer = KafkaProducer(value_serializer=my_serializer)
    value = {
        'key1': 'val1',
        'key2': 'val2'
    }
    producer.send(value)