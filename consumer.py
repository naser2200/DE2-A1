from pulsar import Client, ConsumerType
import threading

# Define the number of consumer threads
num_consumers = 4

# Define a function to process messages
def process_messages(consumer):
    while True:
        msg = consumer.receive()

        try:
            # Decode the message payload
            sentence = msg.data().decode('utf-8')

            # Split the sentence into words
            words = sentence.split()

            # Convert each word to uppercase
            uppercase_words = [word.upper() for word in words]

            # Merge the words back together into a sentence
            uppercase_sentence = ' '.join(uppercase_words)

            # Print the original sentence and the uppercase sentence
            print(f'Received message: {sentence}')
            print(f'Uppercase message: {uppercase_sentence}')

            # Acknowledge the message to remove it from the topic
            consumer.acknowledge(msg)

        except Exception as e:
            # Log the exception and continue consuming messages
            print(f'Error processing message: {e}')

# Create a Pulsar client
client = Client('pulsar://localhost:6650')

# Create multiple consumer instances
consumers = []
for i in range(num_consumers):
    consumer = client.subscribe('my-topic', subscription_name='my-subscription', consumer_type=ConsumerType.Shared)
    consumers.append(consumer)

# Start a thread for each consumer
threads = []
for consumer in consumers:
    thread = threading.Thread(target=process_messages, args=(consumer,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Close the consumers and the Pulsar client
for consumer in consumers:
    consumer.close()
client.close()
