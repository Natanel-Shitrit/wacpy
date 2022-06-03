from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Error:
    
    code: int
    """
    Error code.
    """

    title: str
    """
    Error title.
    """

    details: str
    """
    Error details.
    """