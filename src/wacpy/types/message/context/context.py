from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional

@dataclass_json
@dataclass
class Context:

    message_id: str
    """
    Required.

    The ID of a previous message you are replying to.
    """