from dataclasses import dataclass
from typing import Optional


@dataclass
class Reply:

    id: str
    """
    Unique ID of a selected button / list item.
    """

    title: str
    """
    Title of a selected button / list item.
    """

    description: Optional[str] = None
    """
    Description of the selected row (only for list items).
    """