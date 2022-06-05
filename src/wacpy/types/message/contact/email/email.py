from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Email:
    
    email: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Email address
    """

    type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Standard Values: HOME, WORK
    """
