from ...media import Media

from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Header:
    
    type: str
    """
    Required.

    The header type you would like to use.

    Supported Options:
        • text: Used for List Messages and Reply Buttons.
        • video: Used for Reply Buttons.
        • image: Used for Reply Buttons.
        • document: Used for Reply Buttons.
    """

    text: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required if type is set to text.

    Text for the header.
    Formatting allows emojis, but not markdown.

    Maximum length: 60 characters.
    """

    video: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required if type is set to video.

    Contains the media object for this video.
    """

    image: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required if type is set to image.

    Contains the media object for this image.
    """

    document: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required if type is set to document.

    Contains the media object for this document.
    """