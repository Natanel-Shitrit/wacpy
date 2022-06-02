from dataclasses import dataclass


@dataclass
class Metadata:
    
    display_phone_number: str
    """
    The phone number that is displayed for a business.
    """

    phone_number_id: str
    """
    ID for the phone number.
    A business can respond to a message using this ID.
    """