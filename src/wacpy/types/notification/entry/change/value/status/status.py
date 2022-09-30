from typing import List, Optional
from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field

from .billing import Billing
from .conversation import Conversation
from ..error import Error

@dataclass_json
@dataclass
class Status:
    """
    For a status to be read, it must have been delivered.

    In some scenarios, such as when a user is in the chat screen and a message arrives,
    the message is delivered and read almost simultaneously.

    In this or other similar scenarios, the delivered notification will not be sent back,
    as it is implied that a message has been delivered if it has been read.
    
    The reason for this behavior is internal optimization.
    """

    id: str
    """
    The ID for the message that the business that is subscribed to the webhooks sent to a customer.
    """

    recipient_id: str
    """
    The WhatsApp ID for the customer that the business, that is subscribed to the webhooks, sent to the customer.
    """

    status: str
    """
    delivered - A webhook is triggered when a message received by a business has been delivered.
    read - A webhook is triggered when a message received by a business has been read.
    sent - A webhook is triggered when a business receives a message from a customer.
    """

    timestamp: str
    """
    Date for the status message.
    """

    pricing: Optional[Billing] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    An object containing billing information.
    """

    conversation: Optional[Conversation] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Information about the conversation.
    """

    errors: Optional[List[Error]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    An array of error objects.
    """
