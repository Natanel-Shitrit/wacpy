from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Media:
    
    id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type is audio, document, image, sticker, or video and you are not using a link.

    The media object ID.
    
    Do not use this field when the message type is set to text.
    """

    link: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """       
    Required when type is audio, document, image, sticker, or video and you are not using an uploaded media ID.

    The protocol and URL of the media to be sent.
    Use only with HTTP/HTTPS URLs.

    Do not use this field when the message type is set to text.
    """

    caption: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Describes the specified image or video media.

    Do not use with audio, document, or sticker media.
    """

    filename: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Describes the filename for the specific document.
    
    Use only with document media.
    
    The extension of the filename will specify what format the document is displayed as in WhatsApp.
    """