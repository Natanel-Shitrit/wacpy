from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List

from .entry import Entry

@dataclass_json
@dataclass
class Notification:
    
    object: str
    """
    The specific webhook a business is subscribed to.
    
    The webhook is whatsapp_business_account
    """

    entry: List[Entry]
    """
    An array containing objects:

        id - The WhatsApp Business Account ID for the business that is subscribed to the webhook

        changes (array of objects) - The changes that triggered the webhook

            value (object) - The details for the changes
            See the Value Object table in the next section.

            field - The type of notification.
            The only option for this API is messages.
    """