from dataclasses import dataclass


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