from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Origin:
    
    type: str
    """
    Indicates where a conversation has started.
    This can also be referred to as a conversation entry point

    business_initiated - Indicates that the conversation started by a business sending the first message to a customer.
    This applies any time it has been more than 24 hours since the last customer message.

    customer_initiated - Indicates that the conversation started by a business replying to a customer message.
    This applies only when the business reply is within 24 hours of the last customer message.

    referral_conversion - Indicates that the conversation originated from a free entry point.
    These conversations are always customer-initiated.
    """