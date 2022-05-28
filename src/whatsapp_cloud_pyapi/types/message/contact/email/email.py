from dataclasses import dataclass
from typing import Optional


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
