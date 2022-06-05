from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import List, Optional

from .error import Error
from .message import Message
from .metadata import Metadata
from .contact import Contact
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

    statuses: Optional[List[Status]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Status for a message that was sent by the business that is subscribed to the webhook.
    """

    messages: Optional[List[Message]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Information about a message received by the business that is subscribed to the webhook.
    """

    contacts: Optional[List[Contact]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    The information for the customer who sent a message to the business.
    """

    errors: Optional[List[Error]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Error information received when a message failed.
    """