from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from optparse import Option
from typing import Optional


@dataclass_json
@dataclass
class System:
    
    body: str
    """
    Describes the change to the customer's identity or phone number.
    """

    identity: str
    """
    Hash for the identity fetched from server.
    """

    type: str
    """
    Type of system update. Will be one of the following:

        • customer_changed_number - A customer changed their phone number
        • customer_identity_changed - A customer changed their profile information
    """

    customer: str
    """
    The WhatsApp ID for the customer prior to the update.
    """

    new_wa_id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    New WhatsApp ID for the customer when their phone number is updated.

    Available on webhook versions V11 and below.
    """

    wa_id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    New WhatsApp ID for the customer when their phone number is updated.
    
    Available on webhook versions V12 and above
    """