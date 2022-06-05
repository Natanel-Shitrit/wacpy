from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
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

    name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Name of the location.
    """

    address: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Address of the location.
    
    Only displayed if name is present.
    """