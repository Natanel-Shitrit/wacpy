from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
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