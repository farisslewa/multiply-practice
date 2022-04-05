'''
this code will connect to kafka multiply topic and produce messages.
'''

from confluent_kafka import Producer


broker = "127.0.0.1:9092"
topic = "multiply"
producer = None

producer = Producer({
            'bootstrap.servers': broker,
            'socket.timeout.ms': 100,
            'api.version.request': 'false',
            'broker.version.fallback': '0.9.0',
        }
        )

def send_msg_async(msg):
    print("Send message synchronously")
    producer.produce(topic, msg)
    producer.flush()


#SENDING DATA TO KAFKA TOPIC
message = "Hello this message will be sent to the kafka topic multiply."
send_msg_async(message)