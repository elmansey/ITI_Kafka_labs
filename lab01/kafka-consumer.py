from kafka import KafkaConsumer

# create consumer instance
consumer = KafkaConsumer(
    'iti', # specify topic name
    bootstrap_servers=['localhost:9092'], # specify Kafka broker address
    auto_offset_reset='earliest'
)

# consume messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")