import logging
import random


from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse

import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Gauge, generate_latest, REGISTRY

random_number_metric = Gauge("random_number_total", "Randomly generated number.")


app = FastAPI()

@app.get("/")
async def root():
    random_number = random.randint(1, 21)
    logging.warning(f"Random Number is: {random_number}")
    random_number_metric.set(random_number)
    return f"Random Number is: {random_number}"


@app.get("/metrics", response_class=PlainTextResponse)
async def random_num():
    return generate_latest(random_number_metric)


