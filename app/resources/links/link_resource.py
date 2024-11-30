from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dto.links.link_dto import LinkDto
from yt_dlp import YoutubeDL
import uuid

router = APIRouter()

@router.post("/links")
async def links(linkData: LinkDto):

    # TODO : Setup queue system using redis to setup limitation in DL in // 
    # TODO : setup cache ( get video from bucket is already known )
    # TODO : store downloaded video into S3 or firebase

    options = {
        "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
        "noplaylist": True,
        "http-chunk-size": 10*1024*1024, # 10MB
    }

    with YoutubeDL(options) as ydl:
        ydl.download([linkData.url])

    return JSONResponse(content={"message": f"{linkData.url}"}, status_code=200)