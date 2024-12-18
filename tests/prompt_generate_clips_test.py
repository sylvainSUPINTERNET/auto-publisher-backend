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