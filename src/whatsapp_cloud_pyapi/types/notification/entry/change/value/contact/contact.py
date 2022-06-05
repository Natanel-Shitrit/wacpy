from dataclasses_json import dataclass_json
from dataclasses import dataclass

from .profile import Profile


@dataclass_json
@dataclass
class Contact:
    
    profile: Profile
    """
    The customer's name.
    """

    wa_id: str
    """
    The customer's WhatsApp ID. A business can respond to a message using this ID.
    """