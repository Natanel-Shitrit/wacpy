from .component import Component
from .language import Language

from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
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

    components: Optional[List[Component]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional.

    Array of components objects containing the parameters of the message.
    """