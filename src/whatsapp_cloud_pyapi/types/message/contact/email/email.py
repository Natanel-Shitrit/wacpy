from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Email:
    
    email: Optional[str] = None
    """
    Optional.

    Email address
    """

    type: Optional[str] = None
    """
    Optional.

    Standard Values: HOME, WORK
    """
