from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class Request(BaseModel):
    query: str

@app.post("/chat")
async def chat(req: Request):
    response = agent.invoke({"input": req.query})
    return {"response": response}

@app.get("/")
def root():
    return {"status": "ok"}
