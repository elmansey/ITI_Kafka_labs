from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


# publish a message to a Kafka topic
message = b'Hello, Kafka!'
producer.send('iti', value=message)

# flush the producer to make sure all messages are sent
producer.flush()