from yt_dlp import YoutubeDL
import uuid

def download_yt_video(link:str)->str:
    video_uuid = str(uuid.uuid4())
    options = {
        "verbose": True,
        # "outtmpl" : "downloads/"+str(uuid.uuid4())+"%(title)s.%(ext)s",
        # "outtmpl" : "downloads/"+str(uuid.uuid4())+".%(ext)s",
        "outtmpl" : "downloads/"+video_uuid+".%(ext)s",
        "noplaylist": True,
        "http-chunk-size": 10*1024*1024, # 10MB
    }
    
    with YoutubeDL(options) as ydl:

        # info = ydl.extract_info(link, download=False)
        # print(info)
        
        ydl.download([link])
    
    return f"{video_uuid}"