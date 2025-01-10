import srt

# Exemple de chaîne SRT
srt_string = """
1
00:00:00,000 --> 00:00:13,120
Je pense qu'il aurait dû bien mesurer ce que signifiait demander une autre nationalité,

2
00:00:13,120 --> 00:00:15,800
parce que nous sommes fiers d'être français.

3
00:00:15,800 --> 00:00:22,760
Qu'est-ce que c'est que ce belge de circonstance qui va avoir une nationalité uniquement pour

4
00:00:22,760 --> 00:00:26,559
faire de l'argent ? Moi je serais belge, ça me vexerait à mort de voir un type pareil,
"""

# Convertir la chaîne SRT en une liste d'objets sous-titres
subtitles = list(srt.parse(srt_string))


# Analyser les sous-titres
for subtitle in subtitles:
    print(f"Start: {subtitle.start}, End: {subtitle.end}, Text: {subtitle.content}")