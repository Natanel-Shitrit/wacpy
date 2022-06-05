from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Context:

    from_: str = field(metadata=config(field_name="from"))
    """
    The WhatsApp ID for the customer who replied to an inbound message.
    """

    id: str
    """
    The message ID for the sent message for an inbound reply.
    """

    forwarded: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Set to true if the message received by the business has been forwarded.
    """

    frequently_forwarded: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Set to true if the message received by the business has been forwarded more than 5 times.
    """