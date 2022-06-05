from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
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