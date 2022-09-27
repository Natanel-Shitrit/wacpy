from .contact import Contact
from .context import Context
from .interactive import Interactive
from .location import Location
from .media import Media
from .template import Template
from .text import Text

from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass_json
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

    type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
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

    context: Optional[Context] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required if replying to any message in the conversation.

    An object containing the ID of a previous message you are replying to.
    """

    status: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    A message's status.

    You can use this field to mark a message as read.
    """

    audio: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=audio.

    A media object containing audio.
    """
    
    document: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=document.

    A media object containing a document.
    """

    image: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=image.

    A media object containing an image.
    """

    sticker: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=sticker.

    A media object containing a sticker.

    Static and animated third-party outbound stickers are supported in addition to all types of inbound stickers.
    A static sticker needs to be 512x512 pixels and cannot exceed 100 KB.
    An animated sticker must be 512x512 pixels and cannot exceed 500 KB.

    We support static third-party outbound stickers and all types of inbound stickers.
    The sticker needs to be 512x512 pixels and the file size needs to be less than 100 KB.
    """

    video: Optional[Media] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=video.

    A media object containing a video.
    """

    contacts: Optional[List[Contact]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=contacts.

    A contact object.
    """

    interactive: Optional[Interactive] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=interactive.

    An interactive object.
    This option is used to send List Messages and Reply Buttons.

    The components of each interactive object generally follow a consistent pattern: header, body, footer, and action.
    """

    location: Optional[Location] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=location.

    A location object.
    """

    template: Optional[Template] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required when type=template.

    A template object.
    """

    text: Optional[Text] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required for text messages.

    A text object.
    """