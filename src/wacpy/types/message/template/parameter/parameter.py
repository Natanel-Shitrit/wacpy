from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Parameter:
    type: str
    """
    Required.

    Describes the parameter type.

    Supported Options::
        • text
        • currency
        • date_time
        • image
        • document
        • video
        
    For text-based templates, the only supported parameter types are text, currency, date_time.
    """

    text: Optional[str]
    """
    Required when type=text.

    The message's text.

    For the header component, the character limit is 60 characters.
    For the body component, the character limit is 1024 characters.
    """