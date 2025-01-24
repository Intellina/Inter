from fastapi import FastAPI

app = FastAPI(title="TensorFlow on Grafana", version="1.0.0")

@app.get("/")
async def FirstRouter():
  """
  Main Router
  """
  return {"result":"TensorFlow on Grafana !"}

@app.post("/logits")
async def GetResult():
  """
  Get TensorFlow Model Result
  """
  return {"result":result}