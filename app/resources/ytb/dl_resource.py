from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dto.links.link_dto import LinkDto
import logging
import json

from yt_dlp import YoutubeDL
import uuid

from workers.app_worker import yt_download_video_task


router = APIRouter()

@router.post("/youtube/dl")
async def links(linkData: LinkDto):
    try:
        # res = (
        #     yt_download_video_task.s("https://youtu.be/WrE4D-uu7YA")  # ==> TODO must be less than 10mins ?
        # )
        # res.apply_async()
        # print(res.get())
        # options = {
        #     "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
        #     "noplaylist": True,
        #     "thu"
        #     "http-chunk-size": 10*1024*1024, # 10MB
        # }

        # with YoutubeDL(options) as ydl:
        #     ydl.download([linkData.url])


        options = {
            # "outtmpl" : "downloads/%(title)s.%(ext)s",
            "outtmpl" : "downloads/%(id)s.%(ext)s",
            "writethumbnail": True,
            # "writeinfojson": True,
            "progress_hooks": [lambda d: print(d)],
            "noplaylist": True,
            "http-chunk-size": 10*1024*1024, # 10MB
        }

        with YoutubeDL(options) as ydl:
            ydl.download([linkData.url])

        
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
    


