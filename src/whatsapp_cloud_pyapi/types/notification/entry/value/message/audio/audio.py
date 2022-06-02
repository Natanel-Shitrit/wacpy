from dataclasses import dataclass


@dataclass
class Audio:
    
    id: str
    """
    ID for the audio file.
    """

    mime_type: str
    """
    Mime type of the audio file.
    """