from dataclasses import dataclass
from typing import Optional


@dataclass
class Phone:
    
    phone: Optional[str] = None
    """
    Optional.

    Automatically populated with the wa_id value as a formatted phone number.
    """

    type: Optional[str] = None
    """
    Optional.

    Standard Values: CELL, MAIN, IPHONE, HOME, WORK
    """

    wa_id: Optional[str] = None
    """
    Optional.

    WhatsApp ID.
    """