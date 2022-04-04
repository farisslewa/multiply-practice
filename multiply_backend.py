'''
THIS IS JUST A PRACTICE CODE FOR RETURING TWO NUMBER AND THEIR MULTIPLICATION RESULT
'''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from confluent_kafka import Producer

class KafkaProducer:
    broker = "kafka:9092"
    topic = "multiply"
    producer = None

    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': self.broker,
            'socket.timeout.ms': 100,
            'api.version.request': 'false',
            'broker.version.fallback': '0.9.0',
        }
        )

    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(
                msg.topic(), msg.partition()))

    def send_msg_async(self, msg):
        print("Send message asynchronously")
        self.producer.produce(
            self.topic,
            msg,
            callback=lambda err, original_msg=msg: self.delivery_report(err, original_msg
                                                                        ),
        )
        self.producer.flush()

    def send_msg_sync(self, msg):
        print("Send message synchronously")
        self.producer.produce(
            self.topic,
            msg,
            callback=lambda err, original_msg=msg: self.delivery_report(
                err, original_msg
            ),
        )
        self.producer.flush()


#SENDING DATA TO KAFKA TOPIC
multiply_producer = KafkaProducer()



app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/multiply")
def multiply(param1: int,param2: int):
  result = param1 * param2
  multiply_producer.send_msg_async(result.json())
  return {"param1": param1, "param2": param2, "result": result}

uvicorn.run(app, host="0.0.0.0", port=8000)
