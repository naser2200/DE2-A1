from pulsar import Client, Producer

client = Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

# Generate messages containing sentences
sentences = ['I want to be capatilized', 'Naser Shabani', 'Apache Pulsar is awesome!']

for sentence in sentences:
    # Publish the message to the topic
    producer.send(sentence.encode('utf-8'))

# Close the producer
producer.close()
