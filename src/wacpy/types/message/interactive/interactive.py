from .action import Action
from .body import Body
from .footer import Footer
from .header import Header

from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Interactive:
    
    type: str
    """
    Required.

    The type of interactive message you want to send.

    Supported Options:
        • list: Use it for List Messages.
        • button: Use it for Reply Buttons.
    """

    action: Action
    """
    Required.

    Action you want the user to perform after reading the message.
    """

    body: Body
    """
    Required.

    The body of the message.
    Emojis and markdown are supported.

    Maximum length: 1024 characters.
    """

    footer: Optional[Footer] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    The footer of the message.
    Emojis and markdown are supported.

    Maximum length: 60 characters.
    """

    header: Optional[Header] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Header content displayed on top of a message.
    
    See header object for more information.
    """


