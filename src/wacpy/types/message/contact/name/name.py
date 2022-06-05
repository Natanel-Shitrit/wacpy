from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Name:
    """
    *At least one of the optional parameters needs to be included along with the formatted_name parameter.
    """

    formatted_name: str
    """
    Required.

    Full name, as it normally appears.
    """

    first_name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional*.

    First name.
    """

    last_name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional*.

    Last name.
    """

    middle_name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional*.

    Middle name.
    """

    suffix: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional*.

    Name suffix.
    """

    prefix: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    Optional*.

    Name prefix.
    """