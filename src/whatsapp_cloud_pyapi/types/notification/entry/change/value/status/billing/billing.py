from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Billing:
    
    category: str
    """
    Indicates the conversation pricing category:

    business_initiated - The business sent a message to a customer more than 24 hours after the last customer message

    referral_conversion - The conversation originated from a free entry point. These conversations are always customer-initiated.

    customer_initiated - The business replied to a customer message within 24 hours of the last customer message
    """

    pricing_model: str
    """
    Type of pricing model used by the business. Current supported value is CBP.
    """

    billable: Optional[bool]
    """
    Deprecated.
    Visit the WhatsApp Changelog for more information.

    Indicates if the given message or conversation is billable.
    Default is true for all conversations, including those inside your free tier limit, except those initiated from free entry points.
    Free entry point conversatsion are not billable, false.
    You will not be charged for free tier limit conversations, but they are considered billable and will be reflected on your invoice.
    """