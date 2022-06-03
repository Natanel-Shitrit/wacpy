from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Sticker:
    
    mime_type: str
    """
    image/webp.
    """

    sha256: str
    """
    Hash for the sticker.
    """

    id: str
    """
    ID for the sticker.
    """