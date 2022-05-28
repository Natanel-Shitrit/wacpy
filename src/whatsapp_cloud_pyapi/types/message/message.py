from .contact import Contact
from .interactive import Interactive
from .location import Location
from .media import Media
from .template import Template
from .text import Text

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Message:
    """
    To send a message, you must first assemble a message object with the content you want to send.
    These are the parameters used to create a message object:
    """

    to: str
    """
    Required.

    WhatsApp ID or phone number for the person you want to send a message to.

    See Phone Numbers, Formatting for more information.
    """

    messaging_product: str = "whatsapp"
    """
    Required.

    Messaging service used for the request. Use "whatsapp".
    """

    recipient_type: str = "individual"
    """
    Optional.

    Currently, you can only send messages to individuals. Set this as individual.

    Default: individual
    """

    type: Optional[str] = None
    """
    Optional.

    The type of message you want to send.

    Default: text

    Supported Options:
        • audio: for audio messages.
        • contacts: for contact messages.
        • document: for document messages.
        • image: for image messages.
        • interactive: for list and reply button messages.
        • location: for location messages.
        • sticker: for sticker messages.
        • template: for template messages. Text and media (images and documents) message templates are supported.
        • text: for text messages.
    """

    audio: Optional[Media] = None
    """
    Required when type=audio.

    A media object containing audio.
    """
    
    document: Optional[Media] = None
    """
    Required when type=document.

    A media object containing a document.
    """

    image: Optional[Media] = None
    """
    Required when type=image.

    A media object containing an image.
    """

    sticker: Optional[Media] = None
    """
    Required when type=sticker.

    A media object containing a sticker. Currently, we support inbound both and outbound stickers:

        • For outbound, we only support static third-party stickers.
        • For inbound, we support all types of stickers.

    The sticker needs to be 512x512 pixels and the file’s size needs to be less than 100 KB.
    """

    video: Optional[Media] = None
    """
    Required when type=video.

    A media object containing a video.
    """

    contacts: Optional[List[Contact]] = None
    """
    Required when type=contacts.

    A contact object.
    """

    interactive: Optional[Interactive] = None
    """
    Required when type=interactive.

    An interactive object.
    This option is used to send List Messages and Reply Buttons.

    The components of each interactive object generally follow a consistent pattern: header, body, footer, and action.
    """

    location: Optional[Location] = None
    """
    Required when type=location.

    A location object.
    """

    template: Optional[Template] = None
    """
    Required when type=template.

    A template object.
    """

    text: Optional[Text] = None
    """
    Required for text messages.

    A text object.
    """