from celery import Celery
import os
from dotenv import load_dotenv
from domain.services.worker_groq.prompt_clip_service import chat_completions
from domain.services.worker_openai.transcribe_service import transcribe
from domain.services.worker_yt_download.yt_task_service import download_yt_video
import logging
import json


load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

app = Celery('tasks', 
             broker=f"{os.getenv('RABBIT_MQ_URL')}",
             backend="rpc://") # TODO use redis or something else, rpc is not scalable, it's just create dogshit temp queue ( just for testing purpose)


"""
     1°) task must be called, download media from youtube
"""
@app.task(queue="yt.download")
def yt_download_video_task(link):
    video_uuid = download_yt_video(link)
    return video_uuid


"""
    2° ) task must be called, transcribe the media ( using word, not segment for "karaoke" approach)
"""
@app.task(queue="whisper.transcribe")
def whisper_transcribe(video_uuid:str):
    transcription = transcribe(video_uuid)
    return transcription


"""
    3° ) task must be called, generate prompt clips from the transcription provided
"""
@app.task(queue="groq.completion")
def groq_completion(transcription):
    json_result:dict = chat_completions(transcription)

    logging.debug(json.dumps(json_result, indent=4))

    return {"json_result": json_result, "transcription_srt": transcription}

"""
    4°) Add subtilte to the video
    srt to ass and add to the video
"""
@app.task(queue="ffmpeg.subtitle")
def ffmpeg_add_subtitle(completion_result:dict):
    clips_timestamps = json.loads(completion_result["json_result"]["choices"][0]["message"]["content"])
    logging.debug(json.dumps(clips_timestamps, indent=4))

    print(completion_result["transcription_srt"])

    # find "between" using json and srt 
    # use start and end to cut the clip and fusion the srt found ( using ffmpeg)
    
    pass


# from celery import Celery, chain
# from celery.result import AsyncResult
# import os
# import logging
# from dotenv import load_dotenv
# from time import sleep
# from uuid import uuid4

# load_dotenv()

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

# app = Celery(
#     "auto-publisher-tasks",
#     broker=f"{os.getenv('RABBIT_MQ_URL')}",
#     backend="rpc://" # maybe use redis or something else to get status saved
# )

# @app.task(queue="task1")
# def step1(data, job_id):
#     print(f"{job_id} - step 1 working ...")
#     sleep(5)
#     notify_user(job_id, "step 1 done")
#     return "step1-OK"

# @app.task(queue="task2")
# def step2(data, job_id):
#     print(f"{job_id} - step 2 working ...")
#     sleep(5)
#     notify_user(job_id, "step 2 done")
#     return "step2-OK"

# def notify_user(job_id, msg):
#     print(f"GUI - notify - {job_id} - {msg}")




# # main
# print("starting")
# job_id = str(uuid4())
# workflow = chain(
#     step1.s({"data": "data1"}, job_id),
#     step2.s({"data": "data2"}, job_id)
# )

# res = workflow.apply_async()
# while not res.ready():
#     sleep(1)
#     print("waiting")


# # workflow.apply_async()
# # print(f"Starting workflow for job_id: {job_id}")

# # while True:
# #     sleep(1)
# #     result = AsyncResult(job_id)
# #     print(f"{job_id} : {result.status}")
# #     # if result.ready():
# #     #     print("Workflow done")
        
# #     pass






## TODO 

# from celery import Celery, chain

# app = Celery('app_worker', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# @app.task
# def step_1(x):
#     # Simulate some work
#     send_update_to_gui('step_1', f"Step 1 started with value: {x}")
#     result = x + 1
#     send_update_to_gui('step_1', f"Step 1 completed with result: {result}")
#     return result

# @app.task
# def step_2(y):
#     send_update_to_gui('step_2', f"Step 2 started with value: {y}")
#     result = y * 2
#     send_update_to_gui('step_2', f"Step 2 completed with result: {result}")
#     return result

# @app.task
# def step_3(z):
#     send_update_to_gui('step_3', f"Step 3 started with value: {z}")
#     result = z - 3
#     send_update_to_gui('step_3', f"Step 3 completed with result: {result}")
#     return result

# # Define a function to launch the chain
# def launch_chain(initial_value):
#     workflow = chain(step_1.s(initial_value) | step_2.s() | step_3.s())
#     workflow.apply_async()
#     print("Chain launched!")