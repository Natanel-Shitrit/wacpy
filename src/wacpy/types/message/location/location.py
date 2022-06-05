from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional

@dataclass_json
@dataclass
class Location:

    longitude: float
    """
    Required.

    Longitude of the location.
    """

    latitude: float
    """
    Required.

    Latitude of the location.
    """

    name: Optional[str] = None
    """
    Optional.

    Name of the location.
    """

    address: Optional[str] = None
    """
    Optional.

    Address of the location.
    
    Only displayed if name is present.
    """