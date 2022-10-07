from wacpy.bot.base_bot import BaseWhatsAppBot
from wacpy.types import Message, Notification, message, notification


def WhatsAppEchoBot(BaseWhatsAppBot):
    """
    The WhatsApp Echo Bot is a sample webhook server application that echoes back to you whatever you send it.
    It can serve as a basic reference for how to set up webhooks and reply to incoming messages.
    """

    def on_notification(self, notification: Notification):
        for entry in notification.entry:
            for change in entry.changes:
                if change.value.messages is not None:
                    [self.handle_message(message, contact) for message, contact in zip(
                        change.value.messages, change.value.contacts)]

    def handle_message(self,
                       message: notification.entry.change.value.Message,
                       contact: notification.entry.change.value.Contact):
        # Get message type handler.
        try:
            handler = getattr(self, f"handle_{message.type}_message")
        except AttributeError:
            return

        # Call the handler with the message type object.
        handler(message)

    def handle_text_message(self,
                            message: notification.entry.change.value.Message):
        self.send_message(
            Message(
                to=message.from_,
                text=message.text
            )
        )
