from typing import TypedDict, List


class TranscriptionSegment(TypedDict):
    start: str
    end: str
    text: str

class TranscriptionWord(TypedDict):
    word: str
    start: str
    end: str


class TranscriptionWordAndSegments(TypedDict):
    duration: str
    language: str
    text: str
    segments: List[TranscriptionSegment]
    words: List[TranscriptionWord]
