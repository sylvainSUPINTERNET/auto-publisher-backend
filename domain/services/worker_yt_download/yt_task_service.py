from yt_dlp import YoutubeDL
import uuid

def download_yt_video(link:str)->str:
    options = {
        "verbose": True,
        "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
        "noplaylist": True,
        "http-chunk-size": 10*1024*1024, # 10MB
    }
    with YoutubeDL(options) as ydl:
        ydl.download([link])
    
    # TODO
    return "s3_url.mp4"
