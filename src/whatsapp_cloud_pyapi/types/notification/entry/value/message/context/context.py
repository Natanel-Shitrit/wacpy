from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Context:
    
    forwarded: bool
    """
    Set to true if the message received by the business has been forwarded.
    """

    frequently_forwarded: bool
    """
    Set to true if the message received by the business has been forwarded more than 5 times.
    """

    # TODO: when adding `dataclasses_json` use this:
    # from_: str = field(metadata=config(field_name="from"))
    from_: str
    """
    The WhatsApp ID for the customer who replied to an inbound message.
    """

    id: str
    """
    The message ID for the sent message for an inbound reply.
    """