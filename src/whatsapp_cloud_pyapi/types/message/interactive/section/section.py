from .row import Row

from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional, List


@dataclass_json
@dataclass
class Section:
    
    title: str
    """
    Required if the message has more than one section.

    Title of the section.

    Maximum length: 24 characters.
    """

    rows: Optional[List[Row]] = None
    """
    Required for List Messages.

    Contains a list of rows.
    You can have a total of 10 rows across your sections.

    Each row must have a title (Maximum length: 24 characters) and an ID (Maximum length: 200 characters).
    You can add a description (Maximum length: 72 characters), but it is optional.
    """