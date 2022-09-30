from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .value import Value

@dataclass_json
@dataclass
class Change:

    value: Value
    """
    Value of the change.
    """

    field: str
    """
    The type of the notification.

    The only option for this API is `messages`.
    """