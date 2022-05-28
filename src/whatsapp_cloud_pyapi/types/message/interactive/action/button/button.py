from .reply import Reply

from dataclasses import dataclass


@dataclass
class Button:
    
    reply: Reply
    """
    Required.

    Button content.
    """

    type: str = "reply"
    """
    Required.

    only supported type is reply (for Reply Button)
    """