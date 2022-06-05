from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Footer:
    
    text: str
    """
    Required if the footer object is present.

    The footer content.
    Emojis and markdown are supported.
    Links are supported.

    Maximum length: 60 characters
    """