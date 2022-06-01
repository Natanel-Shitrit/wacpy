from dataclasses import dataclass


@dataclass
class Button:
    
    payload: str
    """
    The payload for a button set up by the business that a customer clicked as part of an interactive message.
    """

    text: str
    """
    Button text.
    """