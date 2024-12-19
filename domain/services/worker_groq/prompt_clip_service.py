
from domain.types.base_type import TranscriptionResultWordsGranularity

def format_transcription_result(transcript_result:TranscriptionResultWordsGranularity)->str:
    # TODO clean data to have something similar to the prompt provided
    return ""

def prompt_generate_clips(transcript_result:TranscriptionResultWordsGranularity):

    formatted = format_transcription_result(transcript_result)

    # TODO => use formatted into prompt as variable
    # TODO => add in prompt something to regroup word
    # TODO => add another task to add highlight on text for each frame of video

    prompt = """
    You are an expert video editor who can read video transcripts and perform video editing.
    Given a transcript with segments, your task is to identify all the conversations related to a user query. 
    Follow these guidelines when choosing conversations. 
    A group of continuous segments in the transcript is a conversation. 
    
    Guidelines: 
    1. The conversation should be relevant to the user query. The conversation should include more than one segment to provide context and continuity. 
    2. Include all the before and after segments needed in a conversation to make it complete. 
    3. The conversation should not cut off in the middle of a sentence or idea. 
    4. Choose multiple conversations from the transcript that are relevant to the user query. 
    5. Match the start and end time of the conversations using the segment timestamps from the transcript. 
    6. The conversations should be a direct part of the video and should not be out of context. 


    
    Output format: {{ 'conversations': [{{'start': 's1', 'end': 'e1'}}, {{'start': 's2','end': 'e2'}}] }}. 
    
    
    Transcript : 00:00:00 - 00:00:10 : Bonjour et bienvenue dans cette vidéo ! Aujourd'hui, nous allons vous montrer comment préparer un délicieux smoothie aux fruits. Ce smoothie est parfait pour commencer la journée. 00:00:10 - 00:00:20 : Pour cette recette, vous aurez besoin de quelques ingrédients de base : 1 banane, 100g de fraises, 200ml de lait d'amande, et quelques glaçons. Vous pouvez aussi ajouter du miel si vous aimez un peu plus sucré. 00:00:20 - 00:00:30 : La première étape consiste à mettre tous les ingrédients dans un mixeur. Commencez par la banane, puis ajoutez les fraises et le lait d'amande. 00:00:30 - 00:00:40 : Une fois les ingrédients dans le mixeur, ajoutez les glaçons. Cela rendra votre smoothie bien frais. Vous pouvez ajuster la quantité de glaçons selon votre préférence. 00:00:40 - 00:00:50 : Ensuite, mixez tous les ingrédients à haute vitesse pendant environ 30 secondes, jusqu'à ce que la consistance soit lisse et crémeuse. 00:00:50 - 00:01:00 : Vous pouvez voir que la texture est parfaite, crémeuse et onctueuse. Si vous trouvez que la consistance est trop épaisse, n'hésitez pas à ajouter un peu plus de lait d'amande. 00:01:00 - 00:01:10 : Une fois votre smoothie prêt, vous pouvez le verser dans un verre. Vous pouvez aussi ajouter quelques morceaux de fruits sur le dessus pour la décoration. 00:01:10 - 00:01:20 : Pour une touche encore plus gourmande, vous pouvez ajouter des graines de chia ou un peu de granola sur le dessus. Cela ajoute de la texture et des bienfaits supplémentaires pour la santé. 00:01:20 - 00:01:30 : Et voilà, votre smoothie aux fruits est prêt ! Il est non seulement délicieux, mais aussi très sain. Vous pouvez le déguster immédiatement ou le mettre au réfrigérateur pour plus tard. 00:01:30 - 00:01:40 : Merci d'avoir regardé cette vidéo. J'espère que vous allez essayer cette recette chez vous. N'oubliez pas de vous abonner à notre chaîne pour plus de recettes saines et rapides. À bientôt ! - user query : viral. return only the result, no talking
    """
    return prompt

# TranscriptionVerbose(duration=32.0, language='french', text="Quand je raconte mon histoire, c'est que j'ai eu ce moment de réalisation quand j'avais genre 7-8 ans, où je suis allé vivre une semaine ou deux semaines, je ne sais plus combien de temps c'était, chez un pote. Et mon pote, ses parents, ils avaient un cabinet d'architecture. J'ai comparé ma vie et sa vie. À ce moment-là, mes parents, il y avait un peu de problèmes à la maison, il y avait des problèmes d'études, on n'avait pas beaucoup d'argent. Et donc du coup, j'ai eu un peu ce contraste entre les deux vies. Et je me suis dit, ah, en fait, je suis pauvre. Et ah, en fait, quand t'as de l'argent, c'est mieux. Et donc, depuis que je suis gamin, j'ai envie d'avoir de l'argent à cause de ça. Mais après, je pense que j'ai aussi ma détermination qui m'a été transmise par mon père, qui est quelqu'un de très déterminé et qui m'a éduqué comme ça. Peut-être que c'est aussi dans les gènes. En tout cas, depuis que je suis gamin, je suis toujours déterminé dans ce que je fais. Je kiffe le business et c'est ça que j'ai utilisé pour aller plus loin quand même.", segments=None, words=[TranscriptionWord(end=0.07999999821186066, start=0.0, word='Quand'), TranscriptionWord(end=0.14000000059604645, start=0.07999999821186066, word='je'), TranscriptionWord(end=0.3199999928474426, start=0.14000000059604645, word='raconte'), TranscriptionWord(end=0.5600000023841858, start=0.3199999928474426, word='mon'), TranscriptionWord(end=0.8399999737739563, start=0.5600000023841858, word='histoire'), TranscriptionWord(end=1.2000000476837158, start=1.159999966621399, word='c'), TranscriptionWord(end=1.2000000476837158, start=1.2000000476837158, word='est'), TranscriptionWord(end=1.340000033378601, start=1.2000000476837158, word='que'), TranscriptionWord(end=1.4600000381469727, start=1.340000033378601, word='j'), TranscriptionWord(end=1.4600000381469727, start=1.4600000381469727, word='ai'), TranscriptionWord(end=1.5199999809265137, start=1.4600000381469727, word='eu'), TranscriptionWord(end=1.6799999475479126, start=1.5199999809265137, word='ce'), TranscriptionWord(end=1.7999999523162842, start=1.6799999475479126, word='moment'), TranscriptionWord(end=1.940000057220459, start=1.7999999523162842, word='de'), TranscriptionWord(end=2.3399999141693115, start=1.940000057220459, word='réalisation'), TranscriptionWord(end=2.6600000858306885, start=2.4000000953674316, word='quand'), TranscriptionWord(end=2.799999952316284, start=2.6600000858306885, word='j'), TranscriptionWord(end=2.799999952316284, start=2.799999952316284, word='avais'), TranscriptionWord(end=3.0799999237060547, start=2.799999952316284, word='genre'), TranscriptionWord(end=3.180000066757202, start=3.0799999237060547, word='7'), TranscriptionWord(end=3.380000114440918, start=3.180000066757202, word='8'), TranscriptionWord(end=3.440000057220459, start=3.380000114440918, word='ans'), TranscriptionWord(end=3.619999885559082, start=3.5399999618530273, word='où'), TranscriptionWord(end=3.6600000858306885, start=3.619999885559082, word='je'), TranscriptionWord(end=3.700000047683716, start=3.6600000858306885, word='suis'), TranscriptionWord(end=3.8399999141693115, start=3.700000047683716, word='allé'), TranscriptionWord(end=4.039999961853027, start=3.8399999141693115, word='vivre'), TranscriptionWord(end=4.340000152587891, start=4.039999961853027, word='une'), TranscriptionWord(end=4.71999979019165, start=4.340000152587891, word='semaine'), TranscriptionWord(end=4.880000114440918, start=4.71999979019165, word='ou'), TranscriptionWord(end=5.0, start=4.880000114440918, word='deux'), TranscriptionWord(end=5.159999847412109, start=5.0, word='semaines'), TranscriptionWord(end=5.320000171661377, start=5.260000228881836, word='je'), TranscriptionWord(end=5.320000171661377, start=5.320000171661377, word='ne'), TranscriptionWord(end=5.320000171661377, start=5.320000171661377, word='sais'), TranscriptionWord(end=5.360000133514404, start=5.320000171661377, word='plus'), TranscriptionWord(end=5.480000019073486, start=5.360000133514404, word='combien'), TranscriptionWord(end=5.579999923706055, start=5.480000019073486, word='de'), TranscriptionWord(end=5.579999923706055, start=5.579999923706055, word='temps'), TranscriptionWord(end=5.78000020980835, start=5.579999923706055, word='c'), TranscriptionWord(end=5.78000020980835, start=5.78000020980835, word='était'), TranscriptionWord(end=5.880000114440918, start=5.840000152587891, word='chez'), TranscriptionWord(end=6.199999809265137, start=5.880000114440918, word='un'), TranscriptionWord(end=6.21999979019165, start=6.199999809265137, word='pote'), TranscriptionWord(end=6.579999923706055, start=6.320000171661377, word='Et'), TranscriptionWord(end=6.820000171661377, start=6.579999923706055, word='mon'), TranscriptionWord(end=6.840000152587891, start=6.820000171661377, word='pote'), TranscriptionWord(end=7.300000190734863, start=7.21999979019165, word='ses'), TranscriptionWord(end=7.360000133514404, start=7.300000190734863, word='parents'), TranscriptionWord(end=7.539999961853027, start=7.400000095367432, word='ils'), TranscriptionWord(end=7.599999904632568, start=7.539999961853027, word='avaient'), TranscriptionWord(end=7.78000020980835, start=7.599999904632568, word='un'), TranscriptionWord(end=7.900000095367432, start=7.78000020980835, word='cabinet'), TranscriptionWord(end=8.15999984741211, start=7.900000095367432, word='d'), TranscriptionWord(end=8.479999542236328, start=8.15999984741211, word='architecture'), TranscriptionWord(end=8.619999885559082, start=8.600000381469727, word='J'), TranscriptionWord(end=8.699999809265137, start=8.619999885559082, word='ai'), TranscriptionWord(end=8.920000076293945, start=8.699999809265137, word='comparé'), TranscriptionWord(end=9.239999771118164, start=8.920000076293945, word='ma'), TranscriptionWord(end=9.380000114440918, start=9.239999771118164, word='vie'), TranscriptionWord(end=9.640000343322754, start=9.380000114440918, word='et'), TranscriptionWord(end=9.859999656677246, start=9.640000343322754, word='sa'), TranscriptionWord(end=10.0600004196167, start=9.859999656677246, word='vie'), TranscriptionWord(end=10.239999771118164, start=10.199999809265137, word='À'), TranscriptionWord(end=10.479999542236328, start=10.239999771118164, word='ce'), TranscriptionWord(end=10.479999542236328, start=10.479999542236328, word='moment'), TranscriptionWord(end=10.539999961853027, start=10.479999542236328, word='là'), TranscriptionWord(end=10.720000267028809, start=10.579999923706055, word='mes'), TranscriptionWord(end=10.899999618530273, start=10.720000267028809, word='parents'), TranscriptionWord(end=11.079999923706055, start=11.0600004196167, word='il'), TranscriptionWord(end=11.100000381469727, start=11.079999923706055, word='y'), TranscriptionWord(end=11.100000381469727, start=11.100000381469727, word='avait'), TranscriptionWord(end=11.279999732971191, start=11.100000381469727, word='un'), TranscriptionWord(end=11.279999732971191, start=11.279999732971191, word='peu'), TranscriptionWord(end=11.4399995803833, start=11.279999732971191, word='de'), TranscriptionWord(end=11.600000381469727, start=11.4399995803833, word='problèmes'), TranscriptionWord(end=11.920000076293945, start=11.600000381469727, word='à'), TranscriptionWord(end=11.960000038146973, start=11.920000076293945, word='la'), TranscriptionWord(end=11.960000038146973, start=11.960000038146973, word='maison'), TranscriptionWord(end=12.300000190734863, start=12.15999984741211, word='il'), TranscriptionWord(end=12.300000190734863, start=12.300000190734863, word='y'), TranscriptionWord(end=12.300000190734863, start=12.300000190734863, word='avait'), TranscriptionWord(end=12.479999542236328, start=12.300000190734863, word='des'), TranscriptionWord(end=12.479999542236328, start=12.479999542236328, word='problèmes'), TranscriptionWord(end=12.760000228881836, start=12.479999542236328, word='d'), TranscriptionWord(end=12.979999542236328, start=12.760000228881836, word='études'), TranscriptionWord(end=13.180000305175781, start=13.079999923706055, word='on'), TranscriptionWord(end=13.180000305175781, start=13.180000305175781, word='n'), TranscriptionWord(end=13.180000305175781, start=13.180000305175781, word='avait'), TranscriptionWord(end=13.34000015258789, start=13.180000305175781, word='pas'), TranscriptionWord(end=13.399999618530273, start=13.34000015258789, word='beaucoup'), TranscriptionWord(end=13.65999984741211, start=13.399999618530273, word='d'), TranscriptionWord(end=13.760000228881836, start=13.65999984741211, word='argent'), TranscriptionWord(end=14.0600004196167, start=13.979999542236328, word='Et'), TranscriptionWord(end=14.199999809265137, start=14.0600004196167, word='donc'), TranscriptionWord(end=14.34000015258789, start=14.199999809265137, word='du'), TranscriptionWord(end=14.34000015258789, start=14.34000015258789, word='coup'), TranscriptionWord(end=14.460000038146973, start=14.34000015258789, word='j'), TranscriptionWord(end=14.460000038146973, start=14.460000038146973, word='ai'), TranscriptionWord(end=14.720000267028809, start=14.460000038146973, word='eu'), TranscriptionWord(end=14.84000015258789, start=14.720000267028809, word='un'), TranscriptionWord(end=14.9399995803833, start=14.84000015258789, word='peu'), TranscriptionWord(end=15.020000457763672, start=14.9399995803833, word='ce'), TranscriptionWord(end=15.319999694824219, start=15.020000457763672, word='contraste'), TranscriptionWord(end=15.380000114440918, start=15.319999694824219, word='entre'), TranscriptionWord(end=15.520000457763672, start=15.380000114440918, word='les'), TranscriptionWord(end=15.720000267028809, start=15.520000457763672, word='deux'), TranscriptionWord(end=15.760000228881836, start=15.720000267028809, word='vies'), TranscriptionWord(end=15.920000076293945, start=15.819999694824219, word='Et'), TranscriptionWord(end=15.960000038146973, start=15.920000076293945, word='je'), TranscriptionWord(end=16.139999389648438, start=15.960000038146973, word='me'), TranscriptionWord(end=16.139999389648438, start=16.139999389648438, word='suis'), TranscriptionWord(end=16.18000030517578, start=16.139999389648438, word='dit'), TranscriptionWord(end=16.520000457763672, start=16.299999237060547, word='ah'), TranscriptionWord(end=16.860000610351562, start=16.520000457763672, word='en'), TranscriptionWord(end=16.860000610351562, start=16.860000610351562, word='fait'), TranscriptionWord(end=16.979999542236328, start=16.860000610351562, word='je'), TranscriptionWord(end=17.020000457763672, start=16.979999542236328, word='suis'), TranscriptionWord(end=17.260000228881836, start=17.020000457763672, word='pauvre'), TranscriptionWord(end=17.5, start=17.360000610351562, word='Et'), TranscriptionWord(end=17.780000686645508, start=17.5, word='ah'), TranscriptionWord(end=18.020000457763672, start=17.780000686645508, word='en'), TranscriptionWord(end=18.020000457763672, start=18.020000457763672, word='fait'), TranscriptionWord(end=18.15999984741211, start=18.040000915527344, word='quand'), TranscriptionWord(end=18.219999313354492, start=18.15999984741211, word='t'), TranscriptionWord(end=18.219999313354492, start=18.219999313354492, word='as'), TranscriptionWord(end=18.31999969482422, start=18.219999313354492, word='de'), TranscriptionWord(end=18.420000076293945, start=18.31999969482422, word='l'), TranscriptionWord(end=18.420000076293945, start=18.420000076293945, word='argent'), TranscriptionWord(end=18.6200008392334, start=18.520000457763672, word='c'), TranscriptionWord(end=18.6200008392334, start=18.6200008392334, word='est'), TranscriptionWord(end=18.84000015258789, start=18.6200008392334, word='mieux'), TranscriptionWord(end=18.959999084472656, start=18.84000015258789, word='Et'), TranscriptionWord(end=19.219999313354492, start=18.959999084472656, word='donc'), TranscriptionWord(end=19.34000015258789, start=19.260000228881836, word='depuis'), TranscriptionWord(end=19.399999618530273, start=19.34000015258789, word='que'), TranscriptionWord(end=19.440000534057617, start=19.399999618530273, word='je'), TranscriptionWord(end=19.479999542236328, start=19.440000534057617, word='suis'), TranscriptionWord(end=19.65999984741211, start=19.479999542236328, word='gamin'), TranscriptionWord(end=19.780000686645508, start=19.719999313354492, word='j'), TranscriptionWord(end=19.799999237060547, start=19.780000686645508, word='ai'), TranscriptionWord(end=19.8799991607666, start=19.799999237060547, word='envie'), TranscriptionWord(end=20.059999465942383, start=19.8799991607666, word='d'), TranscriptionWord(end=20.059999465942383, start=20.059999465942383, word='avoir'), TranscriptionWord(end=20.18000030517578, start=20.059999465942383, word='de'), TranscriptionWord(end=20.280000686645508, start=20.18000030517578, word='l'), TranscriptionWord(end=20.34000015258789, start=20.280000686645508, word='argent'), TranscriptionWord(end=20.479999542236328, start=20.34000015258789, word='à'), TranscriptionWord(end=20.600000381469727, start=20.479999542236328, word='cause'), TranscriptionWord(end=20.8799991607666, start=20.600000381469727, word='de'), TranscriptionWord(end=20.8799991607666, start=20.8799991607666, word='ça'), TranscriptionWord(end=21.1200008392334, start=21.100000381469727, word='Mais'), TranscriptionWord(end=21.459999084472656, start=21.1200008392334, word='après'), TranscriptionWord(end=21.540000915527344, start=21.540000915527344, word='je'), TranscriptionWord(end=21.65999984741211, start=21.540000915527344, word='pense'), TranscriptionWord(end=21.780000686645508, start=21.65999984741211, word='que'), TranscriptionWord(end=21.860000610351562, start=21.780000686645508, word='j'), TranscriptionWord(end=21.899999618530273, start=21.860000610351562, word='ai'), TranscriptionWord(end=22.0, start=21.899999618530273, word='aussi'), TranscriptionWord(end=22.1200008392334, start=22.0, word='ma'), TranscriptionWord(end=22.639999389648438, start=22.1200008392334, word='détermination'), TranscriptionWord(end=22.760000228881836, start=22.639999389648438, word='qui'), TranscriptionWord(end=22.8799991607666, start=22.760000228881836, word='m'), TranscriptionWord(end=22.8799991607666, start=22.8799991607666, word='a'), TranscriptionWord(end=23.0, start=22.8799991607666, word='été'), TranscriptionWord(end=23.360000610351562, start=23.0, word='transmise'), TranscriptionWord(end=23.5, start=23.360000610351562, word='par'), TranscriptionWord(end=23.700000762939453, start=23.5, word='mon'), TranscriptionWord(end=23.8799991607666, start=23.700000762939453, word='père'), TranscriptionWord(end=24.079999923706055, start=24.079999923706055, word='qui'), TranscriptionWord(end=24.280000686645508, start=24.079999923706055, word='est'), TranscriptionWord(end=24.399999618530273, start=24.280000686645508, word='quelqu'), TranscriptionWord(end=24.440000534057617, start=24.399999618530273, word='un'), TranscriptionWord(end=24.579999923706055, start=24.440000534057617, word='de'), TranscriptionWord(end=24.68000030517578, start=24.579999923706055, word='très'), TranscriptionWord(end=25.079999923706055, start=24.68000030517578, word='déterminé'), TranscriptionWord(end=25.200000762939453, start=25.079999923706055, word='et'), TranscriptionWord(end=25.280000686645508, start=25.200000762939453, word='qui'), TranscriptionWord(end=25.360000610351562, start=25.280000686645508, word='m'), TranscriptionWord(end=25.3799991607666, start=25.360000610351562, word='a'), TranscriptionWord(end=25.639999389648438, start=25.3799991607666, word='éduqué'), TranscriptionWord(end=25.81999969482422, start=25.639999389648438, word='comme'), TranscriptionWord(end=25.959999084472656, start=25.81999969482422, word='ça'), TranscriptionWord(end=26.1200008392334, start=26.1200008392334, word='Peut'), TranscriptionWord(end=26.1200008392334, start=26.1200008392334, word='être'), TranscriptionWord(end=26.260000228881836, start=26.1200008392334, word='que'), TranscriptionWord(end=26.260000228881836, start=26.260000228881836, word='c'), TranscriptionWord(end=26.260000228881836, start=26.260000228881836, word='est'), TranscriptionWord(end=26.3799991607666, start=26.260000228881836, word='aussi'), TranscriptionWord(end=26.5, start=26.3799991607666, word='dans'), TranscriptionWord(end=26.65999984741211, start=26.5, word='les'), TranscriptionWord(end=26.81999969482422, start=26.65999984741211, word='gènes'), TranscriptionWord(end=27.040000915527344, start=26.920000076293945, word='En'), TranscriptionWord(end=27.040000915527344, start=27.040000915527344, word='tout'), TranscriptionWord(end=27.040000915527344, start=27.040000915527344, word='cas'), TranscriptionWord(end=27.219999313354492, start=27.15999984741211, word='depuis'), TranscriptionWord(end=27.31999969482422, start=27.219999313354492, word='que'), TranscriptionWord(end=27.3799991607666, start=27.31999969482422, word='je'), TranscriptionWord(end=27.420000076293945, start=27.3799991607666, word='suis'), TranscriptionWord(end=27.559999465942383, start=27.420000076293945, word='gamin'), TranscriptionWord(end=27.68000030517578, start=27.6200008392334, word='je'), TranscriptionWord(end=27.700000762939453, start=27.68000030517578, word='suis'), TranscriptionWord(end=27.8799991607666, start=27.700000762939453, word='toujours'), TranscriptionWord(end=28.219999313354492, start=27.8799991607666, word='déterminé'), TranscriptionWord(end=28.299999237060547, start=28.219999313354492, word='dans'), TranscriptionWord(end=28.399999618530273, start=28.299999237060547, word='ce'), TranscriptionWord(end=28.459999084472656, start=28.399999618530273, word='que'), TranscriptionWord(end=28.540000915527344, start=28.459999084472656, word='je'), TranscriptionWord(end=28.65999984741211, start=28.540000915527344, word='fais'), TranscriptionWord(end=28.899999618530273, start=28.84000015258789, word='Je'), TranscriptionWord(end=29.020000457763672, start=28.899999618530273, word='kiffe'), TranscriptionWord(end=29.18000030517578, start=29.020000457763672, word='le'), TranscriptionWord(end=29.520000457763672, start=29.18000030517578, word='business'), TranscriptionWord(end=29.700000762939453, start=29.520000457763672, word='et'), TranscriptionWord(end=29.81999969482422, start=29.700000762939453, word='c'), TranscriptionWord(end=29.81999969482422, start=29.81999969482422, word='est'), TranscriptionWord(end=29.940000534057617, start=29.81999969482422, word='ça'), TranscriptionWord(end=30.0, start=29.940000534057617, word='que'), TranscriptionWord(end=30.079999923706055, start=30.0, word='j'), TranscriptionWord(end=30.139999389648438, start=30.079999923706055, word='ai'), TranscriptionWord(end=30.399999618530273, start=30.139999389648438, word='utilisé'), TranscriptionWord(end=31.0, start=30.399999618530273, word='pour'), TranscriptionWord(end=31.18000030517578, start=31.0, word='aller'), TranscriptionWord(end=31.34000015258789, start=31.18000030517578, word='plus'), TranscriptionWord(end=31.440000534057617, start=31.34000015258789, word='loin'), TranscriptionWord(end=31.600000381469727, start=31.440000534057617, word='quand'), TranscriptionWord(end=31.639999389648438, start=31.600000381469727, word='même')], task='transcribe')