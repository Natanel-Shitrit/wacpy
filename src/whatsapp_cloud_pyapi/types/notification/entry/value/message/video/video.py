from dataclasses_json import dataclass_json
from dataclasses import dataclass
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

    caption: Optional[str] = None
    """
    The caption for the video, if provided.
    """