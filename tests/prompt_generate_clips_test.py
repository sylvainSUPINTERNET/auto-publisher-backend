import json
import re
from datetime import datetime, timedelta
import srt
import pysubs2

def test_hero():

    result_completion_json = None
    with open("tests/fixtures/result_completion.json") as f:
        result_completion_json = json.load(f)

    ass_str_list = [str]

    subtitles = None
    with open("tests/fixtures/result_completion.srt", 'r', encoding="utf-8") as result_completion_srt:
        subtitles = list(srt.parse(result_completion_srt))

    for sub_obj in result_completion_json:
        subs = pysubs2.SSAFile()
        subs.styles["Default"] = pysubs2.SSAStyle(fontname="Arial", fontsize=20, primarycolor="&H00FFFFFF")

        start_at = srt.srt_timestamp_to_timedelta(sub_obj["start"])
        end_at = srt.srt_timestamp_to_timedelta(sub_obj["end"])

        print(f"SEGMENT START : {start_at}")
        for subtitle in subtitles:
            if subtitle.start in (start_at, end_at) or subtitle.end in (start_at, end_at):
                print(f" {subtitle.start} - {subtitle.end}  {subtitle.content}") 
                subs.append(pysubs2.SSAEvent(start=timestr_to_ms(f"{subtitle.start}"), end=timestr_to_ms(f"{subtitle.end}"), text=f"{subtitle.content}"))
        print(f"SEGMENT END : {end_at}")
        ass_str_list.append(subs.to_string("ass"))
    

    for a in ass_str_list:
        print(a)
        print("========")


def timestr_to_ms(timestr):
    """
    Convert format srt "H:MM:SS.ssssss" in ms (int).
    Ex : "0:00:33.639000" -> 33639
    """
    pattern = r"^(?P<h>\d+):(?P<m>\d+):(?P<s>\d+(?:\.\d+)?)$"
    match = re.match(pattern, timestr)
    if not match:
        raise ValueError(f"Format invalid : '{timestr}'")

    h = int(match.group("h"))
    m = int(match.group("m"))
    s = float(match.group("s"))

    total_seconds = h * 3600 + m * 60 + s
    total_ms = int(total_seconds * 1000)
    return total_ms

# # Créer un nouvel objet de sous-titres
# subs = pysubs2.SSAFile()

# # Ajouter un style (facultatif, utilise 'Default' par défaut)
# subs.styles["Default"] = pysubs2.SSAStyle(fontname="Arial", fontsize=20, primarycolor="&H00FFFFFF")

# # Ajouter des sous-titres
# subs.append(pysubs2.SSAEvent(start=1000, end=3000, text="Bonjour, le monde!"))
# subs.append(pysubs2.SSAEvent(start=4000, end=6000, text="Voici un exemple de sous-titre."))

# # Sauvegarder au format ASS

# ass_string = subs.to_string("ass")
# print(ass_string)


        # start_at = srt.srt_timestamp_to_timedelta(sub_obj["start"])
        # end_at = srt.srt_timestamp_to_timedelta(sub_obj["end"])
        # for subtitle in subtitles:
        #     if subtitle >= start_at or subtitle <= end_at:
        #         print(subtitle.content)
        #     print(" ========= ")

    # for subtitle in subtitles:
        # print(f"Start: {subtitle.start}, End: {subtitle.end}, Text: {subtitle.content}")


        # for l in result_completion_srt:
        #     match = re.match(pattern="(.*)(?:-->)(.*)", string=l)
        #     if match :
        #         print(match.group(1), match.group(2))
        #         # start = convert_srt_timestamp_to_datetime(match.group(1))
        #         # end = convert_srt_timestamp_to_datetime(match.group(2))
        #         # if start == input_start and end <= input_end:
        #         #     print(start, end)
        #         #     break
        #         # print(start, end)


    # print(result_completion_srt)



# def test_build_prompt():
#     with open("tests/fixtures/transcription_segments_words.json") as f:
#         transcription_verbose_fixture = json.load(f)
        
#         prompt_generate_clips(transcript_result=transcription_verbose_fixture)



# # content of test_sample.py
# def inc(x):
#     return x + 1

# from openai import TranscriptionVerbose, TranscriptionWord


# from some_module import TranscriptionVerbose, TranscriptionWord
#     TranscriptionVerbose(duration=32.0, language='french', text="Quand je raconte mon histoire, c'est que j'ai eu ce moment de réalisation quand j'avais genre 7-8 ans, où je suis allé vivre une semaine ou deux semaines, je ne sais plus combien de temps c'était, chez un pote. Et mon pote, ses parents, ils avaient un cabinet d'architecture. J'ai comparé ma vie et sa vie. À ce moment-là, mes parents, il y avait un peu de problèmes à la maison, il y avait des problèmes d'études, on n'avait pas beaucoup d'argent. Et donc du coup, j'ai eu un peu ce contraste entre les deux vies. Et je me suis dit, ah, en fait, je suis pauvre. Et ah, en fait, quand t'as de l'argent, c'est mieux. Et donc, depuis que je suis gamin, j'ai envie d'avoir de l'argent à cause de ça. Mais après, je pense que j'ai aussi ma détermination qui m'a été transmise par mon père, qui est quelqu'un de très déterminé et qui m'a éduqué comme ça. Peut-être que c'est aussi dans les gènes. En tout cas, depuis que je suis gamin, je suis toujours déterminé dans ce que je fais. Je kiffe le business et c'est ça que j'ai utilisé pour aller plus loin quand même.", segments=None, words=[TranscriptionWord(end=0.07999999821186066, start=0.0, word='Quand'), TranscriptionWord(end=0.14000000059604645, start=0.07999999821186066, word='je')])
# def x():
#     TranscriptionVerbose(duration=32.0, language='french', text="Quand je raconte mon histoire, c'est que j'ai eu ce moment de réalisation quand j'avais genre 7-8 ans, où je suis allé vivre une semaine ou deux semaines, je ne sais plus combien de temps c'était, chez un pote. Et mon pote, ses parents, ils avaient un cabinet d'architecture. J'ai comparé ma vie et sa vie. À ce moment-là, mes parents, il y avait un peu de problèmes à la maison, il y avait des problèmes d'études, on n'avait pas beaucoup d'argent. Et donc du coup, j'ai eu un peu ce contraste entre les deux vies. Et je me suis dit, ah, en fait, je suis pauvre. Et ah, en fait, quand t'as de l'argent, c'est mieux. Et donc, depuis que je suis gamin, j'ai envie d'avoir de l'argent à cause de ça. Mais après, je pense que j'ai aussi ma détermination qui m'a été transmise par mon père, qui est quelqu'un de très déterminé et qui m'a éduqué comme ça. Peut-être que c'est aussi dans les gènes. En tout cas, depuis que je suis gamin, je suis toujours déterminé dans ce que je fais. Je kiffe le business et c'est ça que j'ai utilisé pour aller plus loin quand même.", segments=None, words=[TranscriptionWord(end=0.07999999821186066, start=0.0, word='Quand'), TranscriptionWord(end=0.14000000059604645, start=0.07999999821186066, word='je')

# def test_answer():
#     assert inc(3) == 5

# from openai.types.audio.transcription import Transcription

# def test_build_prompt():


#     # {
#     #             "duration": transcription_verbose.duration,
#     #             "language": transcription_verbose.language,
#     #             "text": transcription_verbose.text,
#     #             "words": [
#     #                 {"word": transcription_word.word, "start": transcription_word.start, "end": transcription_word.end}
#     #                 for transcription_word in transcription_verbose.words
#     #                ]            
#     #             }



