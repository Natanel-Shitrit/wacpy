from dataclasses_json import dataclass_json
from dataclasses import dataclass

from .billing import Billing
from .conversation import Conversation

@dataclass_json
@dataclass
class Status:

    conversation: Conversation
    """
    Information about the conversation.
    """
    
    id: str
    """
    The ID for the message that the business that is subscribed to the webhooks sent to a customer.
    """

    pricing: Billing
    """
    An object containing billing information.
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
