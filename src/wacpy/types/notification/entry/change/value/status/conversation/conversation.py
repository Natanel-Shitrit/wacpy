from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional

from .origin import Origin


@dataclass_json
@dataclass
class Conversation:
    """
    WhatsApp defines a conversation as a 24-hour session of messaging between a person and a business.
    There is no limit on the number of messages that can be exchanged in the fixed 24-hour window.
    The 24-hour conversation session begins when:

        • A business-initiated message is delivered to a customer
        • A business reply to a customer message is delivered

    The 24-hour conversation session is different from the 24-hour customer support window.
    The customer support window is a rolling window that is refreshed when a customer-initiated message is delivered to a business.
    Within the customer support window businesses can send free-form messages.
    Any business-initiated message sent more than 24 hours after the last customer message must be a template message.
    """


    id: str
    """
    Represents the ID of the conversation the given status notification belongs to.
    """

    origin: Origin
    """
    Indicates who initiated the conversation.
    """

    expiration_timestamp: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Date when the conversation expires.
    This field is only present for messages with a `status` set to `sent`.
    """