from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Address:
    
    street: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Street number and name
    """

    city: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    City name.
    """

    state: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    State name.
    """

    zip: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    ZIP code.
    """

    country: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Full country name.
    """

    country_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Two-letter country abbreviation.
    """

    type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Address type.

    Standard Values: HOME, WORK
    """