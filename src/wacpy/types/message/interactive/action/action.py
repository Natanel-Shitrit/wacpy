from .button import Button
from ..section import Section

from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass_json
@dataclass
class Action:
    
    button: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required for List Messages.

    Button content.
    It cannot be an empty string and must be unique within the message.
    Emojis are supported, markdown is not.

    Maximum length: 20 characters.
    """

    buttons: Optional[List[Button]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """    	
    Required for Reply Buttons.

    A button can contain the following parameters:

        • type:
            only supported type is reply (for Reply Button)

        • title:
            Button title.
            It cannot be an empty string and must be unique within the message.
            Emojis are supported, markdown is not.
            Maximum length: 20 characters.

        • id:
            Unique identifier for your button.
            This ID is returned in the webhook when the button is clicked by the user.
            Maximum length: 256 characters.
    
    You can have up to 3 buttons.
    
    You cannot have leading or trailing spaces when setting the ID.
    """

    sections: Optional[List[Section]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Required for List Messages.

    Array of section objects.
    There is a minimum of 1 and maximum of 10.
    
    See section object.
    """