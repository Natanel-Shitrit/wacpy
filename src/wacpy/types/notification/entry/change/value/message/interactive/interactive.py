from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional

from .reply import Reply


@dataclass_json
@dataclass
class Interactive:
    
    type: str
    """
    The type of the interactive message.
    """

    button_reply: Optional[Reply] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Sent when a customer clicks a button.
    """

    list_reply: Optional[Reply] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Sent when a customer selects an item from a list.
    """