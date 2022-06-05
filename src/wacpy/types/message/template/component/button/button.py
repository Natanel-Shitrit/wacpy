from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Button:
    
    type: str
    """
    Required.

    Indicates the type of parameter for the button.

    Supported Options:
        • "payload"
        • "text"
    """

    payload: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required for quick_reply buttons.

    Developer-defined payload that is returned when the button is clicked in addition to the display text on the button.

    See Callback from a Quick Reply Button Click for an example.
    """

    text: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required for URL buttons.

    Developer-provided suffix that is appended to the predefined prefix URL in the template.
    """