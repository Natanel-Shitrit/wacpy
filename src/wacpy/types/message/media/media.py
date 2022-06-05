from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Media:
    
    id: Optional[str] = None
    """
    Required when type is audio, document, or image and you are not using a link.

    The media object ID.
    
    Do not use this field when the message type is set to text.
    """

    link: Optional[str] = None
    """       
    Required when type is audio, document, image, video, and sticker and you are not using an uploaded media ID.

    The protocol and URL of the media to be sent.
    Use only with HTTP/HTTPS URLs.

    Do not use this field when the message type is set to text.
    """

    caption: Optional[str] = None
    """
    Optional.

    Describes the specified document or image media.

    Do not use with audio media.
    """

    filename: Optional[str] = None
    """
    Optional.

    Describes the filename for the specific document.
    
    Use only with document media.
    """