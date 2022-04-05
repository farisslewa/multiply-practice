'''
THIS IS JUST A PRACTICE CODE FOR RETURING TWO NUMBER AND THEIR MULTIPLICATION RESULT
It also save a log record in posgresql database
and produce a message to a kafka broker
'''
import uvicorn
import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from confluent_kafka import Producer
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/multiply")
def multiply(param1: float,param2: float):
  conn = psycopg2.connect(
    database="logdb",
    user="user",
    password="password",
    host="logdb"
  )

  result = param1 * param2
  cur = conn.cursor()
  cur.execute(f"INSERT INTO log VALUES ({param1}, {param2}, {result})")
  conn.commit()
  cur.close()
  conn.close()

  broker = "kafka:9092"
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
  #message = "Hello this message will be sent to the kafka topic multiply."
  message = {"param1": param1, "param2": param2, "result": result}
  send_msg_async(json.dumps(message).encode("utf-8"))

  return {"param1": param1, "param2": param2, "result": result}

uvicorn.run(app, host="0.0.0.0", port=8000)
