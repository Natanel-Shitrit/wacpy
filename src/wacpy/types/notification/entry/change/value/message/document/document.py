from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Document:

    filename: str
    """
    Name for the file on the sender's device.
    """

    mime_type: str
    """
    Mime type of the document file.
    """

    id: str
    """
    ID for the document.
    """

    sha256: str
    """
    Hash.
    """

    caption: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Caption for the document, if provided.
    """