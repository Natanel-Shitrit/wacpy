from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Text:
    body: str
    """
    Required for text messages.

    The text of the text message which can contain URLs which begin with http:// or https:// and formatting.

    If you include URLs in your text and want to include a preview box in text messages (preview_url: true),
    make sure the URL starts with http:// or https:// —https:// URLs are preferred.
    
    You must include a hostname, since IP addresses will not be matched.

    Maximum length: 4096 characters
    """

    preview_url: bool = False
    """
    Optional.

    By default, WhatsApp recognizes URLs and makes them clickable,
    but you can also include a preview box with more information about the link.

    Set this field to true if you want to include a URL preview box.


    The majority of the time, the receiver will see a URL they can click on when you send an URL,
    set preview_url to true, and provide a body object with a http or https link.


    URL previews are only rendered after one of the following has happened:

    The business has sent a message template to the user.
    The user initiates a conversation with a "click to chat" link.
    The user adds the business phone number to their address book and initiates a conversation.

    Default: false.
    """