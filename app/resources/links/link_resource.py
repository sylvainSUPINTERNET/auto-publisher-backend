from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dto.links.link_dto import LinkDto
import logging
import json

from yt_dlp import YoutubeDL
import uuid

from infrastructure.rabbitmq_conn import RabbitMqClient
from infrastructure.rabbitmq_queues import RabbitMQQueueEnum

router = APIRouter()

@router.post("/links")
async def links(linkData: LinkDto):
    try:
        logging.info(f"Received link : {linkData.url}, publish to queue : {RabbitMQQueueEnum.YT_DL_QUEUE.value}")

        channel = RabbitMqClient().get_conn().channel()
        channel.basic_publish(exchange='', routing_key=f'{RabbitMQQueueEnum.YT_DL_QUEUE.value}', body=json.dumps({
            "url": linkData.url
        }))
        channel.close()
        return JSONResponse(content={"message": f"{linkData.url}"}, status_code=200)
    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={"message": f"Error occured, please try again"}, status_code=500)

    # TODO : Setup queue system using redis to setup limitation in DL in // 
    # TODO : setup cache ( get video from bucket is already known )
    # TODO : store downloaded video into S3 or firebase


    ##  TOOD : move this into consummer
    # options = {
    #     "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
    #     "noplaylist": True,
    #     "http-chunk-size": 10*1024*1024, # 10MB
    # }

    # with YoutubeDL(options) as ydl:
    #     ydl.download([linkData.url])

    # return JSONResponse(content={"message": f"{linkData.url}"}, status_code=200)
    