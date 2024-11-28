from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx import FadeIn, FadeOut
# Charger la vidéo principale
video = VideoFileClip("sample.mp4")

# Transcription avec phrases horodatées
transcription = [
    {"text": "Hello world, how are you?", "start": 0.0, "end": 2.0},
    {"text": "This is a test.", "start": 2.1, "end": 4.0}
]

# Fonction pour créer un texte
def create_text(word, color="white", fontsize=96):
    return TextClip(text=word, font_size=fontsize, color=color, font="Atop-R99O3.ttf", stroke_color="black", stroke_width=10, margin=(20,20))

# Liste pour stocker les clips texte
text_clips = []

# Générer les mots highlightés
for phrase in transcription:
    phrase_text = phrase["text"]
    start = phrase["start"]
    end = phrase["end"]
    duration = end - start

    # Diviser la phrase en mots
    words = phrase_text.split()
    num_words = len(words)
    word_duration = duration / num_words  # Durée approximative par mot

    # Générer les clips pour chaque mot
    for i, word in enumerate(words):
        word_start = start + i * word_duration
        word_end = word_start + word_duration

        # Texte normal (blanc, visible en permanence)
        # normal_text = create_text(word, color="white").with_position(("center", "bottom")).with_start(0).with_duration(video.duration)

        video_h = video.h
        margin_bottom = 400
        highlighted_text = create_text(word, color="WHITE").with_position(("center", video_h - margin_bottom)).with_start(word_start).with_duration(word_duration)

        # Ajouter les clips
        # text_clips.append(normal_text)  # Texte blanc permanent
        text_clips.append(highlighted_text)  # Highlight dynamique

# Combiner la vidéo principale avec les clips de texte
final_video = CompositeVideoClip([video] + text_clips)

# Exporter la vidéo finale
# final_video.write_videofile("output_highlighted.mp4", fps=24)

final_video.write_videofile("output_highlighted.mp4", codec="libx264", audio_codec="aac", 
                     ffmpeg_params=["-r", "60", "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920", 
                                    "-preset", "ultrafast", "-b:v", "1500k"]) # , "-threads", "4"



# from moviepy import VideoFileClip, TextClip, CompositeVideoClip
# from moviepy.video.fx import FadeIn, FadeOut

# # basic exemple using shit params for low CPU usage

# clip = (
#     VideoFileClip("sample.mp4")
    
    
#      .subclipped(0, 2)
#     # .with_volume_scaled(0.8)

#     # TODO : 9:16
# ).resized(height=720)


# text_clip = (TextClip(font="Atop-R99O3.ttf", text="Hello World", font_size=56, color='white')).with_position(("center", "top")).with_duration(2) #.with_duration(clip.duration)

# new_video = CompositeVideoClip([clip, text_clip])

# # shit laptop
# new_video.write_videofile("shit.mp4", codec="libx264", audio_codec="aac", 
#                      ffmpeg_params=["-r", "60", "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920", 
#                                     "-preset", "ultrafast", "-b:v", "1500k"]) # , "-threads", "4"



# # # good laptop 
# # # new_video.write_videofile(
# # #     "output_tiktok_60fps.mp4",
# # #     codec="libx264",
# # #     audio_codec="aac",
# # #     ffmpeg_params=[
# # #         "-r", "60",  # Fréquence d'images
# # #         "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",  # Mise à l'échelle
# # #         "-preset", "medium",  # Qualité d'encodage
# # #         "-b:v", "4000k",  # Bitrate vidéo
# # #         "-crf", "23",  # Contrôle de qualité
# # #         "-movflags", "faststart",  # Optimisation pour le streaming
# # #         "-profile:v", "high", "-level", "4.2",  # Encodage avancé
# # #         "-b:a", "192k"  # Bitrate audio
# # #     ]
# # # )

