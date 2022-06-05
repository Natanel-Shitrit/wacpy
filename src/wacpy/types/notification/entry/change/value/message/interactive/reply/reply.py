from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
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

    description: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Description of the selected row (only for list items).
    """