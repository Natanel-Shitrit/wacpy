from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional

from .reply import Reply


@dataclass_json
@dataclass
class Interactive:
    
    type: str
    """
    The type of the interactive message.
    """

    button_reply: Optional[Reply]
    """
    Sent when a customer clicks a button.
    """

    list_reply: Optional[Reply]
    """
    Sent when a customer selects an item from a list.
    """