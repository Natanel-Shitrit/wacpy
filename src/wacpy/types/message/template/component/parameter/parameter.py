from .currency import Currency
from .datetime import DateTime
from ....media import Media

from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Parameter:
    type: str
    """
    Required.

    Describes the parameter type.

    Supported Options:
        • text
        • currency
        • date_time
        • image
        • document
        • video
        
    For text-based templates, the only supported parameter types are text, currency, date_time.
    """

    text: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=text.

    The message's text.

    For the header component, the character limit is 60 characters.
    For the body component, the character limit is 1024 characters.
    """

    currency: Optional[Currency] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=currency.

    A currency object.
    """

    date_time: Optional[DateTime] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=date_time.

    A date_time object.
    """

    image: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=image.

    A media object of type image.

    Captions not supported when used in a media template.
    """

    document: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=document.

    A media object of type document.
    Only PDF documents are supported for media-based message templates.
    
    Captions not supported when used in a media template.
    """

    video: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=video.

    A media object of type video.
    
    Captions not supported when used in a media template.
    """