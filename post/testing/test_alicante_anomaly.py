from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "anomalies_alicante_salinity_EA001_36_level"

message = {
    "algorithm": "Border check",
    "value": [6120.0],
    "status": "Error: measurement above upper limit",
    "timestamp": 1641800086654,
    "status_code": -1
}

# 

for i in range(100):
    print(i)
    message["timestamp"] += 10000
    producer.send(topic, value=message)
    sleep(20)