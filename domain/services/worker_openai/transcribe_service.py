
import os
import glob
import logging
from openai import OpenAI


# NOTE : limit media 
"""
, in _request
    raise self._make_status_error_from_response(err.response) from None
openai.APIStatusError: Error code: 413 - {'error': {'message': '413: Maximum content size limit (26214400) exceeded (26383110 bytes read)', 'type': 'server_error', 'param': None, 'code': None}}
"""

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')


def transcribe(video_uuid:str):
    try: 
        client = OpenAI(api_key=f"{os.getenv('OPEN_AI_SECRET_KEY', None)}")

        # TODO replace with S3 at some point
        search_pattern = os.path.join("downloads", f"{video_uuid}.*")
        matching_files = glob.glob(search_pattern)
        if not matching_files:
            raise Exception(f"No file found with UUID: {video_uuid}")
        file_path = matching_files[0]
        _, file_extension = os.path.splitext(file_path)
        full_path = os.path.join("downloads", f"{video_uuid}{file_extension}")
        # TODO replace with S3 at some point

        logging.info(f"Transcribe request for video : {full_path}")

        with open(full_path, "rb") as audio_file:
            transcription_verbose = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,  # Passez le fichier ouvert en mode binaire
                response_format="verbose_json",
                timestamp_granularities=["word"]
            )
            logging.info(f"transcription_verbose : {transcription_verbose}")
            return {
                "duration": transcription_verbose.duration,
                "language": transcription_verbose.language,
                "text": transcription_verbose.text,
                "words": [
                    {"word": transcription_word.word, "start": transcription_word.start, "end": transcription_word.end}
                    for transcription_word in transcription_verbose.words
                   ]            
                }
    except Exception as e:
        logging.error(f"Error during transcription : {e}")


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


# def get_transcription(transcription):
#     if transcription.status == "completed":
#         return transcription.text
#     return None
