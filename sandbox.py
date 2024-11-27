from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# basic exemple using shit params for low CPU usage

clip = (
    VideoFileClip("sample.mp4")
    
    
     .subclipped(0, 2)
    # .with_volume_scaled(0.8)

    # TODO : 9:16
).resized(height=720)


text_clip = (TextClip(font="Atop-R99O3.ttf", text="Hello World", font_size=56, color='white')).with_position(("center", "top")).with_duration(clip.duration)

new_video = CompositeVideoClip([clip, text_clip])

# shit laptop
# new_video.write_videofile("output_tiktok_60fps.mp4", codec="libx264", audio_codec="aac", 
#                      ffmpeg_params=["-r", "60", "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920", 
#                                     "-preset", "ultrafast", "-b:v", "1500k"]) # , "-threads", "4"


new_video.write_videofile(
    "output_tiktok_60fps.mp4",
    codec="libx264",
    audio_codec="aac",
    ffmpeg_params=[
        "-r", "60",  # Fréquence d'images
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",  # Mise à l'échelle
        "-preset", "medium",  # Qualité d'encodage
        "-b:v", "4000k",  # Bitrate vidéo
        "-crf", "23",  # Contrôle de qualité
        "-movflags", "faststart",  # Optimisation pour le streaming
        "-profile:v", "high", "-level", "4.2",  # Encodage avancé
        "-b:a", "192k"  # Bitrate audio
    ]
)

