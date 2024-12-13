from celery import Celery, chain
from celery.result import AsyncResult
import os
import logging
from dotenv import load_dotenv
from time import sleep
from uuid import uuid4

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

app = Celery(
    "auto-publisher-tasks",
    broker=f"{os.getenv('RABBIT_MQ_URL')}",
    backend="rpc://" # maybe use redis or something else to get status saved
)

@app.task(queue="task1")
def step1(data, job_id):
    print(f"{job_id} - step 1 working ...")
    sleep(5)
    notify_user(job_id, "step 1 done")
    return "step1-OK"

@app.task(queue="task2")
def step2(data, job_id):
    print(f"{job_id} - step 2 working ...")
    sleep(5)
    notify_user(job_id, "step 2 done")
    return "step2-OK"

def notify_user(job_id, msg):
    print(f"GUI - notify - {job_id} - {msg}")




# main
print("starting")
job_id = str(uuid4())
workflow = chain(
    step1.s({"data": "data1"}, job_id),
    step2.s({"data": "data2"}, job_id)
)

res = workflow.apply_async()
while not res.ready():
    sleep(1)
    print("waiting")


# workflow.apply_async()
# print(f"Starting workflow for job_id: {job_id}")

# while True:
#     sleep(1)
#     result = AsyncResult(job_id)
#     print(f"{job_id} : {result.status}")
#     # if result.ready():
#     #     print("Workflow done")
        
#     pass
