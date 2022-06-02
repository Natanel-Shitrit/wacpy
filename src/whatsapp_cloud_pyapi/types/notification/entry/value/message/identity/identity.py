from dataclasses import dataclass


@dataclass
class Identity:
    
    acknowledged: str
    """
    State of acknowledgment for the messages system customer_identity_changed.
    """

    created_timestamp: str
    """
    The time when the WhatsApp Business Management API detected the customer may have changed their profile information.
    """

    hash: str
    """
    The ID for the messages system customer_identity_changed.
    """