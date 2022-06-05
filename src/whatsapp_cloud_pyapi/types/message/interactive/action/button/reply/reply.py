from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Reply:

    id: str
    """
    Required.

    Unique identifier for your button.
    This ID is returned in the webhook when the button is clicked by the user.
    
    Maximum length: 256 characters.
    """

    title: str
    """
    Required.

    Button title.

    It cannot be an empty string and must be unique within the message.
    Emojis are supported, markdown is not.
    
    Maximum length: 20 characters.
    """