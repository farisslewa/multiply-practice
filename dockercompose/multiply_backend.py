'''
THIS IS JUST A PRACTICE CODE FOR RETURING TWO NUMBER AND THEIR MULTIPLICATION RESULT
'''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
def multiply(param1: int,param2: int):
  result = param1 * param2
  return {"param1": param1, "param2": param2, "result": result}

uvicorn.run(app, host="0.0.0.0", port=8000)
