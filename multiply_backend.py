'''
THIS IS JUST A PRACTICE CODE FOR RETURING TWO NUMBER AND THEIR MULTIPLICATION RESULT
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/multiply")
def multiply(param1: int,param2: int):
  result = param1 * param2
  return {"param1": param1, "param2": param2, "result": result}
