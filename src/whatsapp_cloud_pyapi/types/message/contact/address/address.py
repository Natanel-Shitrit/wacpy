from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    
    street: Optional[str] = None
    """
    Optional.

    Street number and name
    """

    city: Optional[str] = None
    """
    Optional.

    City name.
    """

    state: Optional[str] = None
    """
    Optional.

    State name.
    """

    zip: Optional[str] = None
    """
    Optional.

    ZIP code.
    """

    country: Optional[str] = None
    """
    Optional.

    Full country name.
    """

    country_code: Optional[str] = None
    """
    Optional.

    Two-letter country abbreviation.
    """

    type: Optional[str] = None
    """
    Optional.

    Address type.

    Standard Values: HOME, WORK
    """