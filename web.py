from fastapi import FastAPI
import uvicorn
from threading import Thread

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bot is running."}

def run():
    uvicorn.run(app, host="0.0.0.0", port=8080)

def keep_alive():
    Thread(target=run).start()
