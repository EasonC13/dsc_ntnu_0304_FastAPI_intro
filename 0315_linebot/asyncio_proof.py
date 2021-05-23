# uvicorn asyncio_proof:app --workers 4 --port 8080

from fastapi import FastAPI

import time
import asyncio
import random
import datetime

app = FastAPI()

unique_int = random.randint(1, 100)

@app.get("/wait")
async def wait_time(second:int = 10):
    out = f"start at {str(datetime.datetime.now())}, "
    time.sleep(second)
    out += f"end at {str(datetime.datetime.now())}"
    return out


@app.get("/asyncio/wait")
async def async_wait_time(second:int = 10):
    out = f"start at {str(datetime.datetime.now())}, "
    await asyncio.sleep(second)
    out += f"end at {str(datetime.datetime.now())}"
    return out

@app.get("/unique-int")
async def proof_multi_worker():
    return unique_int

