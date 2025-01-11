import pysubs2
import re

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







x = timestr_to_ms("0:00:31.840000")
print(x)



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














# import srt

# # Exemple de chaîne SRT
# srt_string = """
# 1
# 00:00:00,000 --> 00:00:13,120
# Je pense qu'il aurait dû bien mesurer ce que signifiait demander une autre nationalité,

# 2
# 00:00:13,120 --> 00:00:15,800
# parce que nous sommes fiers d'être français.

# 3
# 00:00:15,800 --> 00:00:22,760
# Qu'est-ce que c'est que ce belge de circonstance qui va avoir une nationalité uniquement pour

# 4
# 00:00:22,760 --> 00:00:26,559
# faire de l'argent ? Moi je serais belge, ça me vexerait à mort de voir un type pareil,
# """

# # Convertir la chaîne SRT en une liste d'objets sous-titres
# subtitles = list(srt.parse(srt_string))


# # Analyser les sous-titres
# for subtitle in subtitles:
#     print(f"Start: {subtitle.start}, End: {subtitle.end}, Text: {subtitle.content}")