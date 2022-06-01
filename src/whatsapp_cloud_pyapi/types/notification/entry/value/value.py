from dataclasses import dataclass
from typing import List

from .contact import Contact
from .error import Error
from .message import Message
from .metadata import Metadata
from .status import Status


@dataclass
class Value:

    contacts: List[Contact]
    """
    The information for the customer who sent a message to the business.
    """

    errors: List[Error]
    """
    Error information received when a message failed.
    """

    messaging_product: str
    """	
    The value is whatsapp.
    """

    messages: List[Message]
    """
    Information about a message received by the business that is subscribed to the webhook.
    """

    metadata: Metadata
    """
    Metadata for the business that is subscribed to the webhook.
    """

    statuses: List[Status]
    """
    Status for a message that was sent by the business that is subscribed to the webhook.
    """