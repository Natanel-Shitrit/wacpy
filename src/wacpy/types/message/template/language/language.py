from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Language:
    
    policy: str
    """    	
    Required.

    The language policy the message should follow.
    The only supported option is deterministic.
    
    See Language Policy Options.
    https://developers.facebook.com/docs/whatsapp/api/messages/message-templates#language-policy-options
    """

    code: str
    """    	
    Required.

    The code of the language or locale to use.
    Accepts both language and language_locale formats (e.g., en and en_US).

    For all codes, see Supported Languages.
    https://developers.facebook.com/docs/whatsapp/api/messages/message-templates#supported-languages
    """