from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Reaction:
    
    message_id: str
    """
    Required.

    The WhatsApp Message ID (wamid) of the message on which the reaction should appear.
    
    The reaction will not be sent if:
        • The message is older than 30 days
        • The message is a reaction message
        • The message has been deleted

    If the ID is of a message that has been deleted, the message will not be delivered.
    """

    emoji: str
    """
    Required.

    Emoji to appear on the message.

    • All emojis supported by Android and iOS devices are supported.
    • Rendered-emojis are supported.
    • If using emoji unicode values, values must be Java- or JavaScript-escape encoded.
    • Only one emoji can be sent in a reaction message
    • Use an empty string to remove a previously sent emoji.
    """