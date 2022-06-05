from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from typing import List, Optional

from .identity import Identity
from .error import Error
from .image import Image
from .video import Video
from .audio import Audio
from .button import Button
from .context import Context
from .document import Document
from .interactive import Interactive
from .referral import Referral
from .sticker import Sticker
from .system import System
from .text import Text


@dataclass_json
@dataclass
class Message:
    
    from_: str = field(metadata=config(field_name="from"))
    """
    The customer's phone number who sent the message to the business
    """

    id: int
    """
    The ID for the message that was received by the business.
    You could use messages endpoint to mark it as read.
    """

    type: str
    """
    The type of message that has been received by the business that has subscribed to Webhooks.
    
    Possible value can be one of the following:
        • audio
        • button
        • document
        • text
        • image
        • interactive
        • sticker
        • system - for customer number change messages
        • unknown
        • video
    """

    timestamp: str
    """
    The time when the customer sent the message to the business.
    """

    identity: Optional[Identity] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    A webhook is triggered when a customer's phone number or profile information has been updated.
    """

    errors: Optional[List[Error]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    The message that a business received from a customer is not a supported type.
    """

    image: Optional[Image] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When messages type is set to image, this object is included in the messages object.
    """

    video: Optional[Video] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When messages type is set to video, this object is included in messages object.
    """

    audio: Optional[Audio] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When the messages type is set to audio, including voice messages, this object is included in the messages object.
    """

    button: Optional[Button] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When the messages type field is set to button, this object is included in the messages object.
    """

    context: Optional[Context] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When the messages type field is set to button, this object is included in the messages object.
    The context for a message that was forwarded or in an inbound reply from the customer.
    """

    document: Optional[Document] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When messages type is set to document, this object is included in the messages object.
    """

    interactive: Optional[Interactive] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When a customer selected a button or list reply, this object is included in the messages object.
    """

    referral: Optional[Referral] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    A customer clicked an ad that redirects them to WhatsApp, this object is included in the messages object.
    """

    sticker: Optional[Sticker] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When messages type is set to sticker, this object is included in the messages object.
    """

    system: Optional[System] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When messages type is set to system, a customer has updated their phone number or profile information, this object is included in the messages object.
    """

    text: Optional[Text] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    When messages type is set to text, the body of text is included in the messages object.
    """
