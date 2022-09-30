from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Profile:
    
    name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    The customer's name.
    """