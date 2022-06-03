from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Language:
    
    policy: str
    """    	
    Required.

    Default (and only supported option): deterministic
    The language policy the message should follow.
    
    See Language Policy Options for more information.
    """

    code: str
    """    	
    Required.

    The code of the language or locale to use.
    Accepts both language and language_locale formats (e.g., en and en_US).

    See Supported Languages for all codes.
    """