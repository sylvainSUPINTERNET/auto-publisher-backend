import ffmpeg
import uuid


video = "downloads/0f998d04-49c6-4961-910a-32f4bdb685d4.mp4"
output = "outputs/"


ffmpeg.input(video).output(f"{output}{str(uuid.uuid4())}.mp4", vf=f"subtitles=subtitles/test1.ass", ss="00:00:27.56", to="00:01:07.14").run()