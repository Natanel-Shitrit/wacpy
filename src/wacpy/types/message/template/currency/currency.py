from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Currency:
    
    fallback_value: str
    """
    Required.

    Default text if localization fails.
    """

    code: str
    """    	
    Required.

    Currency code as defined in ISO 4217.
    """

    amount_1000: str
    """    	
    Required.

    Amount multiplied by 1000.
    """