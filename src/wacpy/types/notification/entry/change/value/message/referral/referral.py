from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from typing import Optional


@dataclass_json
@dataclass
class Referral:
    
    source_url: str
    """
    A customer clicked an ad that redirects them to WhatsApp, this object is included in the messages object.
    """

    source_type: str
    """
    The type of the ad’s source; ad or post.
    """

    source_id: str
    """
    Meta ID for an ad or a post.
    """

    headline: str
    """
    Headline used in the ad or post.
    """

    body: str
    """
    Body for the ad or post.
    """

    media_type: str
    """
    Media present in the ad or post; image or video
    """

    image_url: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    URL of the image, when media_type is an image
    """

    video_url: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    URL of the video, when media_type is a video
    """

    thumbnail_url: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    """
    URL for the thumbnail, when media_type is a video
    """