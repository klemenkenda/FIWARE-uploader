from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "Device_1efe_pred_output"

message = {
    "algorithm": "Combination",
    "value": [6120.0],
    "status": "Percent score",
    "timestamp": 1641800086654,
    "status_code": 0.0
}

for i in range(100):
    print(i)
    producer.send(topic, value=message)
    sleep(20)