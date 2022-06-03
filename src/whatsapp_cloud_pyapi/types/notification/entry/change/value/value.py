from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List, Optional

from .error import Error
from .message import Message
from .metadata import Metadata
from .profile import Profile
from .status import Status


@dataclass_json
@dataclass
class Value:

    metadata: Metadata
    """
    Metadata for the business that is subscribed to the webhook.
    """
    
    messaging_product: str = "whatsapp"
    """	
    The value is whatsapp.
    """

    statuses: Optional[List[Status]] = None
    """
    Status for a message that was sent by the business that is subscribed to the webhook.
    """

    messages: Optional[List[Message]] = None
    """
    Information about a message received by the business that is subscribed to the webhook.
    """

    contacts: Optional[List[Profile]] = None
    """
    The information for the customer who sent a message to the business.
    """

    errors: Optional[List[Error]] = None
    """
    Error information received when a message failed.
    """