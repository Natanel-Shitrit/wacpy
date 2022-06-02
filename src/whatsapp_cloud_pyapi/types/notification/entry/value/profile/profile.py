from dataclasses import dataclass


@dataclass
class Profile:
    
    name: str
    """
    The customer's name.
    """

    wa_id: str
    """
    The customer's WhatsApp ID. A business can respond to a message using this ID.
    """