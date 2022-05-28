from dataclasses import dataclass


@dataclass
class Body:
    
    text: str
    """
    Required.

    The body content of the message.
    Emojis and markdown are supported.
    Links are supported.

    Maximum length: 1024 characters.
    """