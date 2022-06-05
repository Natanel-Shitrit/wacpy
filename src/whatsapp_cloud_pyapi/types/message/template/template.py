from .component import Component
from .language import Language

from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional, List


@dataclass_json
@dataclass
class Template:
    name: str
    """
    Required.

    Name of the template.
    """
    
    language: Language
    """
    Required.

    Contains a language object.
    Specifies the language the template may be rendered in.

    Only the deterministic language policy works with media template messages.
    """

    components: Optional[List[Component]] = None
    """
    Optional.

    Array of components objects containing the parameters of the message.
    """