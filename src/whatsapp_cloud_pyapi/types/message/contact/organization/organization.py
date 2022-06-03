from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Organization:
    
    company: Optional[str] = None
    """
    Optional.

    Name of the contact's company.
    """
    
    department: Optional[str] = None
    """
    Optional.

    Name of the contact's department.
    """

    title: Optional[str] = None
    """
    Optional.

    Contact's business title.
    """