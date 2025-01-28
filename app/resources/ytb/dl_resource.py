import os
import io
from pathlib import Path

import botocore
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dto.links.link_dto import LinkDto
import logging
import json

from yt_dlp import YoutubeDL
import uuid

from workers.app_worker import yt_download_video_task
import boto3

router = APIRouter()


s3 = boto3.client(
    service_name ="s3",
    endpoint_url = f"{os.getenv('CLOUDFLARE_R2_ENDPOINT_URL')}",
    aws_access_key_id = f"{os.getenv('CLOUDFLARE_R2_ACCESS_KEY')}",
    aws_secret_access_key = f"{os.getenv('CLOUDFLARE_R2_SECRET_KEY')}",
    region_name=f"{os.getenv('CLOUDFLARE_R2_REGION')}", # Must be one of: wnam, enam, weur, eeur, apac, auto
)

file_path = Path(__file__).parent/"downloads"


@router.post("/youtube/dl")
async def links(linkData: LinkDto):

    # TODO : implement 
    linkData.url = "https://www.youtube.com/watch?v=nDwSDh6kCX0"
    # TODO : download as "file" and send the byte 
    file_name = "Se lever tôt ne te rendra pas meilleur (et c'est tant mieux).webm"


    # TODO : compress video before sending it to the client ( without reducing the quality )
    try:    
        with s3.head_object(Bucket=f"{os.getenv('CLOUDFLARE_R2_BUCKET_NAME')}", Key=f"{file_name}") as obj:
            # start worker (file is already in bucket)
            logging.info("File already in bucket, starting worker")
            # TODO : start worker
            pass
    except botocore.exceptions.ClientError as e:
        if e.response.get("ResponseMetadata").get("HTTPStatusCode") == 404:
            # download the file
            logging.info("File not found, download process started")
            file_path = file_path/file_name

            with file_path.open("rb") as f:
                s3.upload_fileobj(io.BytesIO(f.read()),f"{os.getenv('CLOUDFLARE_R2_BUCKET_NAME')}", file_name)
            # TODO : start worker 
            pass
        else:
            return JSONResponse(content={"message": f"Error occured, please try again"}, status_code=200)
    
    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={"message": f"Error occured, please try again"}, status_code=500)



    # try:
    #     # res = (
    #     #     yt_download_video_task.s("https://youtu.be/WrE4D-uu7YA")  # ==> TODO must be less than 10mins ?
    #     # )
    #     # res.apply_async()
    #     # print(res.get())
    #     # options = {
    #     #     "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
    #     #     "noplaylist": True,
    #     #     "thu"
    #     #     "http-chunk-size": 10*1024*1024, # 10MB
    #     # }

    #     # with YoutubeDL(options) as ydl:
    #     #     ydl.download([linkData.url])


    #     options = {
    #         # "outtmpl" : "downloads/%(title)s.%(ext)s",
    #         "outtmpl" : "downloads/%(id)s.%(ext)s",
    #         "writethumbnail": True,
    #         # "writeinfojson": True,
    #         "progress_hooks": [lambda d: print(d)],
    #         "noplaylist": True,
    #         "http-chunk-size": 10*1024*1024, # 10MB
    #     }

    #     with YoutubeDL(options) as ydl:
    #         ydl.download([linkData.url])

        
    #     return JSONResponse(content={"message": f"{linkData.url}"}, status_code=200)
    # except Exception as e:
    #     logging.error(str(e))
    #     return JSONResponse(content={"message": f"Error occured, please try again"}, status_code=500)

    # # TODO : Setup queue system using redis to setup limitation in DL in // 
    # # TODO : setup cache ( get video from bucket is already known )
    # # TODO : store downloaded video into S3 or firebase


    # ##  TOOD : move this into consummer
    # # options = {
    # #     "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
    # #     "noplaylist": True,
    # #     "http-chunk-size": 10*1024*1024, # 10MB
    # # }

    # # with YoutubeDL(options) as ydl:
    # #     ydl.download([linkData.url])

    # # return JSONResponse(content={"message": f"{linkData.url}"}, status_code=200)
    


