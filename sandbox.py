from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# basic exemple using shit params for low CPU usage

clip = (
    VideoFileClip("sample.mp4")
    
    
     .subclipped(0, 2)
    # .with_volume_scaled(0.8)

    # TODO : 9:16
).resized(height=720)


text_clip = (TextClip(font="Atop-R99O3.ttf", text="Hello World", font_size=70, color='white', font_size="caption")).with_position(("center", "top")).with_duration(clip.duration)

new_video = CompositeVideoClip([clip, text_clip])

# new_video.write_videofile("output.mp4", ffmpeg_params=["-preset", "ultrafast"] ) # use dogshit params ( consume CPU extremly !)
#                           #codec="libx264", fps=24)

new_video.write_videofile("output_tiktok_60fps.mp4", codec="libx264", audio_codec="aac", 
                     ffmpeg_params=["-r", "60", "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920", 
                                    "-preset", "ultrafast", "-b:v", "1500k"]) # , "-threads", "4"