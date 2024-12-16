# import os
# from openai import OpenAI
# import dotenv

# dotenv.load_dotenv()

# client = OpenAI(
#     api_key=f"{os.getenv('OPEN_AI_SECRET_KEY', None)}"
# )


# # limit media 

# """
# , in _request
#     raise self._make_status_error_from_response(err.response) from None
# openai.APIStatusError: Error code: 413 - {'error': {'message': '413: Maximum content size limit (26214400) exceeded (26383110 bytes read)', 'type': 'server_error', 'param': None, 'code': None}}
# """


# # video_file = open("./5mins_audio.mp3", "rb")
# video_file = open("./test_yom.webm", "rb")

# transcription = client.audio.transcriptions.create(
#     model="whisper-1",
#     file=video_file, 
#     response_format="verbose_json",
#     # timestamp_granularities=["segment"] # word
#     timestamp_granularities=["word"] 
#     )


# print(transcription)
# print(transcription.segments) # None with word granularity

