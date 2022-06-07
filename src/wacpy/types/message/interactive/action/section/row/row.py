from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Row:

    id: str
    """
    Required.

    Unique identifier for this row.

    Maximum length: 200 characters.
    """

    title: str
    """
    Required.

    Title of the row.

    Maximum length: 24 characters.
    """

    description: Optional[str]
    """
    Optional.

    Description of the row.

    Maximum length: 72 characters.
    """