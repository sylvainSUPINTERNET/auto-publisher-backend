import pysubs2

def convert_srt_to_ass(input_srt, output_ass):

    subs = pysubs2.load(input_srt, encoding="utf-8")
    
    subs.styles["Default"] = pysubs2.SSAStyle(
        fontname="Arial",
        fontsize=28,
        primarycolor=pysubs2.Color(255, 255, 255, 0),  # white
        outlinecolor=pysubs2.Color(0, 0, 0, 0),        # black
        # borderstyle=1
        # outline=2,
        # shadow=0
    )
    
    subs.save(output_ass)

# Exemple d'utilisation
convert_srt_to_ass("result.srt", "result.ass")
