from dataclasses import dataclass
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


@dataclass
class Message:
    
    # TODO: when adding `dataclasses_json` use this:
    # from_: str = field(metadata=config(field_name="from"))
    from_: str
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

    identity: Identity
    """
    A webhook is triggered when a customer's phone number or profile information has been updated.
    """

    errors: List[Error]
    """
    The message that a business received from a customer is not a supported type.
    """

    timestamp: int
    """
    The time when the customer sent the message to the business.
    """

    image: Optional[Image] = None
    """
    When messages type is set to image, this object is included in the messages object.
    """

    video: Optional[Video] = None
    """
    When messages type is set to video, this object is included in messages object.
    """

    audio: Optional[Audio] = None
    """
    When the messages type is set to audio, including voice messages, this object is included in the messages object.
    """

    button: Optional[Button] = None
    """
    When the messages type field is set to button, this object is included in the messages object.
    """

    context: Optional[Context] = None
    """
    When the messages type field is set to button, this object is included in the messages object.
    The context for a message that was forwarded or in an inbound reply from the customer.
    """

    document: Optional[Document] = None
    """
    When messages type is set to document, this object is included in the messages object.
    """

    interactive: Optional[Interactive] = None
    """
    When a customer selected a button or list reply, this object is included in the messages object.
    """

    referral: Optional[Referral] = None
    """
    A customer clicked an ad that redirects them to WhatsApp, this object is included in the messages object.
    """

    sticker: Optional[Sticker] = None
    """
    When messages type is set to sticker, this object is included in the messages object.
    """

    system: Optional[System] = None
    """
    When messages type is set to system, a customer has updated their phone number or profile information, this object is included in the messages object.
    """

    text: Optional[Text] = None
    """
    When messages type is set to text, the body of text is included in the messages object.
    """
