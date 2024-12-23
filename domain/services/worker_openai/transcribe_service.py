
import os
import glob
import logging
from openai import OpenAI
import json

from domain.types.base_type import TranscriptionWordAndSegments


# NOTE : limit media 
"""
, in _request
    raise self._make_status_error_from_response(err.response) from None
openai.APIStatusError: Error code: 413 - {'error': {'message': '413: Maximum content size limit (26214400) exceeded (26383110 bytes read)', 'type': 'server_error', 'param': None, 'code': None}}
"""

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')


def transcribe(video_uuid:str)->TranscriptionWordAndSegments:
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
                timestamp_granularities=["word", "segment"]
            )
            logging.info(f"transcription_verbose : {transcription_verbose}")

            result = {
                "duration": f"{transcription_verbose.duration}",
                "language": f"{transcription_verbose.language}",
                "text": f"{transcription_verbose.text}",
                "segments": [
                    {"start": f"{segment.start}", "end": f"{segment.end}", "text": f"{segment.text}"}
                    for segment in transcription_verbose.segments
                ],
                "words": [
                    {"start": f"{word.start}", "end": f"{word.end}", "word": f"{word.word}"}
                    for word in transcription_verbose.words
                ]
            }
            
            logging.debug(json.dumps(result, indent=4))
                
            return result
    except Exception as e:
        logging.error(f"Error during transcription : {e}")
