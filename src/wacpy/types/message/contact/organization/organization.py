from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Organization:
    
    company: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Name of the contact's company.
    """
    
    department: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Name of the contact's department.
    """

    title: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Contact's business title.
    """