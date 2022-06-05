from .reply import Reply

from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
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