from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Video:

    filename: str
    """
    The name for the file on the sender's device.
    """

    mime_type: str
    """
    The mime type for the video file.
    """

    id: str
    """
    The ID for the video.
    """

    sha256: str
    """
    The hash for the video.
    """

    caption: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    The caption for the video, if provided.
    """