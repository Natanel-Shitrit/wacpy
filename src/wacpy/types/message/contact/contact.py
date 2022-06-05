from .address import Address
from .email import Email
from .name import Name
from .organization import Organization
from .phone import Phone
from .url import URL

from typing import Optional, List
from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field

@dataclass_json
@dataclass
class Contact:
    
    name: Name
    """
    Required.

    Full contact name — see name object.
    """

    adresses: Optional[List[Address]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Full contact address(es) — see address object.
    """

    birthday: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    YYYY-MM-DD formatted string.
    """

    emails: Optional[List[Email]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Contact email address(es) — see email object.
    """

    org: Optional[Organization] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Contact organization information — see org object.
    """

    phones: Optional[List[Phone]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Contact phone number(s) — see phone object.
    """

    urls: Optional[List[URL]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Contact URL(s) — see url object.
    """