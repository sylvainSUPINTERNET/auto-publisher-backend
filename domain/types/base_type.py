from typing import TypedDict, List

class TranscriptionWord(TypedDict):
    word: str
    start: str
    end: str
    
class TranscriptionResultWordsGranularity(TypedDict):
    duration: str
    language: str
    text: str
    words: List[TranscriptionWord]

