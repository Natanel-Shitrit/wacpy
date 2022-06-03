from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Image:
    
    mime_type: str
    """
    Mime type for the image.
    """

    id: str
    """
    ID for the image.
    """

    sha256: str
    """
    Image hash.
    """

    caption: Optional[str] = None
    """
    Caption for the image, if provided.
    """