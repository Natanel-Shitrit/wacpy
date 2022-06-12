from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
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

    description: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Description of the row.

    Maximum length: 72 characters.
    """