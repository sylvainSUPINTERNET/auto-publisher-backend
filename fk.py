# from moviepy import VideoFileClip, TextClip, CompositeVideoClip
# from moviepy.video.tools.subtitles import SubtitlesClip

# # TextClip generator function to style subtitles
# generator = lambda text: TextClip(text, font="Atop-R99O3.ttf", font_size=24, color='white')

# # Create SubtitlesClip using the SRT file
# sub = SubtitlesClip("test.srt", make_textclip=generator, encoding='utf-8')

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings


change_settings({"IMAGEMAGICK_BINARY": r'C:\Users\syjoly\scoop\apps\imagemagick\7.1.1-43\magick.exe'})

generator = lambda txt: TextClip(txt, font='Atop-R99O3.ttf', fontsize=24, color='white')
subs = SubtitlesClip('test.srt', generator)
subtitles = SubtitlesClip(subs, generator)

video = VideoFileClip("downloads/4baad131-26b2-413c-afb1-53b1b03a9928.mp4").subclip(5.940000057220459, 12.119999885559082)
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("output.mp4")




# sub = SubtitlesClip("test.srt", font='Georgia-Regular', make_textclip=generator, encoding='utf-8')
# clip = (
#     VideoFileClip("downloads/4baad131-26b2-413c-afb1-53b1b03a9928.mp4").subclipped(5.940000057220459, 12.119999885559082)
# )
# final = CompositeVideoClip([clip, subtitles])
# final.write_videofile("final.mp4", fps=myvideo.fps)





# end=12.119999885559082, no_speech_prob=0.33263033628463745, seek=0, start=5.46000003814697

# """
# Je pense qu'il aurait dû bien mesurer ce que signifiait demander une autre nationalité


#  words=[TranscriptionWord(end=5.940000057220459, start=5.460000038146973, word='Je'), TranscriptionWord(end=6.420000076293945, start=5.940000057220459, word='pense'), TranscriptionWord(end=6.71999979019165, start=6.420000076293945, word='qu'), TranscriptionWord(end=6.71999979019165, start=6.71999979019165, word='il'), TranscriptionWord(end=6.71999979019165, start=6.71999979019165, word='aurait'), TranscriptionWord(end=6.860000133514404, start=6.71999979019165, word='dû'), TranscriptionWord(end=7.239999771118164, start=6.860000133514404, word='bien'), TranscriptionWord(end=8.239999771118164, start=7.239999771118164, word='mesurer'), TranscriptionWord(end=8.619999885559082, start=8.239999771118164, word='ce'), TranscriptionWord(end=8.760000228881836, start=8.619999885559082, word='que'), TranscriptionWord(end=9.619999885559082, start=8.760000228881836, word='signifiait'), TranscriptionWord(end=10.34000015258789, start=9.619999885559082, word='demander'), TranscriptionWord(end=11.319999694824219, start=10.34000015258789, word='une'), TranscriptionWord(end=11.520000457763672, start=11.319999694824219, word='autre'), TranscriptionWord(end=12.119999885559082, start=11.520000457763672, word='nationalité')
# """ 


# segment_text="Je pense qu'il aurait dû bien mesurer ce que signifiait demander une autre nationalité"
# words = [
#     {
#         "end": 5.940000057220459,
#         "start": 5.460000038146973,
#         "word": "Je"
#     },
#     {
#         "end": 6.420000076293945,
#         "start": 5.940000057220459,
#         "word": "pense"
#     },
#     {
#         "end": 6.71999979019165,
#         "start": 6.420000076293945,
#         "word": "qu"
#     },
#     {
#         "end": 6.71999979019165,
#         "start": 6.71999979019165,
#         "word": "il"
#     },
#     {
#         "end": 6.71999979019165,
#         "start": 6.71999979019165,
#         "word": "aurait"
#     },
#     {
#         "end": 6.860000133514404,
#         "start": 6.71999979019165,
#         "word": "dû"
#     },
#     {
#         "end": 7.239999771118164,
#         "start": 6.860000133514404,
#         "word": "bien"
#     },
#     {
#         "end": 8.239999771118164,
#         "start": 7.239999771118164,
#         "word": "mesurer"
#     },
#     {
#         "end": 8.619999885559082,
#         "start": 8.239999771118164,
#         "word": "ce"
#     },
#     {
#         "end": 8.760000228881836,
#         "start": 8.619999885559082,
#         "word": "que"
#     },
#     {
#         "end": 9.619999885559082,
#         "start": 8.760000228881836,
#         "word": "signifiait"
#     },
#     {
#         "end": 10.34000015258789,
#         "start": 9.619999885559082,
#         "word": "demander"
#     },
#     {
#         "end": 11.319999694824219,
#         "start": 10.34000015258789,
#         "word": "une"
#     },
#     {
#         "end": 11.520000457763672,
#         "start": 11.319999694824219,
#         "word": "autre"
#     },
#     {
#         "end": 12.119999885559082,
#         "start": 11.520000457763672,
#         "word": "nationalité"
#     }
# ]


# def generate_colored_text(f):
#     for word in words:
#         print(f"WORD {word['start']} <= {f} <= {word['end']}")
#         if word["start"] <= f <= word["end"]:
#             return "red"
#     return "black"

# clip = (
#     VideoFileClip("downloads/4baad131-26b2-413c-afb1-53b1b03a9928.mp4").subclipped(5.940000057220459, 12.119999885559082)
# )

# # full text of segment
# txt_clip = TextClip(
#     font="Atop-R99O3.ttf",
#     text=segment_text,
#     font_size=15,
#     color='white',
#     method=lambda t: generate_colored_text(t),
# ).with_duration(clip.duration).with_position('center')


# final_clip = CompositeVideoClip([clip, txt_clip])
# final_clip.write_videofile("result.mp4")

# # clip = CompositeVideoClip([clip, txt_clip])
# # final_video = CompositeVideoClip([clip, txt_clip])
# # final_video.write_videofile("result.mp4")

