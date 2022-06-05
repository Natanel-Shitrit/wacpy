from dataclasses_json import dataclass_json
from dataclasses import dataclass
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

    first_name: Optional[str] = None
    """
    Optional*.

    First name.
    """

    last_name: Optional[str] = None
    """
    Optional*.

    Last name.
    """

    middle_name: Optional[str] = None
    """
    Optional*.

    Middle name.
    """

    suffix: Optional[str] = None
    """
    Optional*.

    Name suffix.
    """

    prefix: Optional[str] = None
    """
    Optional*.

    Name prefix.
    """