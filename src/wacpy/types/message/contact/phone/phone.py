from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Phone:
    
    phone: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Automatically populated with the wa_id value as a formatted phone number.
    """

    type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Standard Values: CELL, MAIN, IPHONE, HOME, WORK
    """

    wa_id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    WhatsApp ID.
    """