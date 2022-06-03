from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List

from .change import Change

@dataclass_json
@dataclass
class Entry:

    id: str
    """
    The WhatsApp Business Account ID for the business that is subscribed to the webhook
    """

    changes: List[Change]
    """
    The details for the changes.
    """