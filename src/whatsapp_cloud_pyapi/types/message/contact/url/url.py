from dataclasses import dataclass
from typing import Optional


@dataclass
class URL:
    
    url: Optional[str] = None
    """
    Optional.

    URL.
    """

    type: Optional[str] = None
    """
    Optional.

    Standard Values: HOME, WORK
    """