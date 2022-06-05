from .address import Address
from .email import Email
from .name import Name
from .organization import Organization
from .phone import Phone
from .url import URL

from typing import Optional, List
from dataclasses_json import dataclass_json
from dataclasses import dataclass

@dataclass_json
@dataclass
class Contact:
    
    name: Name
    """
    Required.

    Full contact name — see name object.
    """

    adresses: Optional[List[Address]] = None
    """
    Optional.

    Full contact address(es) — see address object.
    """

    birthday: Optional[str] = None
    """
    Optional.

    YYYY-MM-DD formatted string.
    """

    emails: Optional[List[Email]] = None
    """
    Optional.

    Contact email address(es) — see email object.
    """

    org: Optional[Organization] = None
    """
    Optional.

    Contact organization information — see org object.
    """

    phones: Optional[List[Phone]] = None
    """
    Optional.

    Contact phone number(s) — see phone object.
    """

    urls: Optional[List[URL]] = None
    """
    Optional.

    Contact URL(s) — see url object.
    """