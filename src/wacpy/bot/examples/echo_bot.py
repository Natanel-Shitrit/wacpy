from wacpy.bot.base_bot import BaseWhatsAppBot
from wacpy.types import Message, Notification, message, notification


class WhatsAppEchoBot(BaseWhatsAppBot):
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


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('phone_id')
    parser.add_argument('access_token')
    parser.add_argument('verify_token')
    parser.add_argument('webhook_path')
    parser.add_argument('--app_secret', default=None,
                        help='app secret used for verifying payloads')
    parser.add_argument('--bind', '-b', metavar='ADDRESS', default='',
                        help='specify alternate bind address '
                             '(default: all interfaces)')
    parser.add_argument('--port', '-p', action='store', default=8000, type=int,
                        nargs='?',
                        help='specify alternate port (default: 8000)')
    args = parser.parse_args()

    WhatsAppEchoBot(
        phone_id=args.phone_id,
        access_token=args.access_token
    ).activate_webhook(
        bind_address=args.bind,
        port=args.port,
        # request handler parameters:
        verify_token=args.verify_token,
        webhook_path=args.webhook_path,
        app_secret=args.app_secret
    )
