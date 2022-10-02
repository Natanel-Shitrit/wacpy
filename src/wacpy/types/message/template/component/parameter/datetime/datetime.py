from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class DateTime:
    
    fallback_value: str
    """
    Required.

    Default text.
    
    For Cloud API, we always use the fallback value, and we do not attempt to localize using other optional fields.
    """