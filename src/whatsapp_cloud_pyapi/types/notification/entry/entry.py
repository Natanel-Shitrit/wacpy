from dataclasses import dataclass
from typing import List
from .value import Value

@dataclass
class Entry:

    id: str
    """
    The WhatsApp Business Account ID for the business that is subscribed to the webhook
    """

    changes: List[Value]
    """
    The details for the changes.
    """