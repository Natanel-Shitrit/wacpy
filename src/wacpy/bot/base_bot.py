import abc
import functools
import hashlib
import hmac
import http.client
import http.server
import json
import urllib.parse
from typing import Any, Dict, Optional

from .. import WA_CLOUD_API_COMPATIBILITY
from ..types import Message, Notification

class BasicWhatsAppRequestHandler(http.server.BaseHTTPRequestHandler):
    '''
    The basic request handler for BaseWhatsAppBot.

    The request handler of BaseWhatsAppBot should handle
    the following incoming requests according to the official documentations:

    1. GET requests will always be used for webhook verification.
        https://developers.facebook.com/docs/graph-api/webhooks/getting-started#verification-requests

    2. POST requests will always be used for notifications.
        https://developers.facebook.com/docs/graph-api/webhooks/getting-started#event-notifications
    '''

    def __init__(self, bot, *args, **kwargs):
        # Bot instance to call on notification.
        self.__bot: BaseWhatsAppBot = bot
        # Extra parameters:
        self.__verify_token = kwargs.pop('verify_token')
        self.__webhook_path = kwargs.pop('webhook_path')
        self.__app_secret = kwargs.pop('app_secret', None)

        if self.__app_secret is None:
            # TODO: replace with logging.
            print('App secret is not configured - payloads will not be validated,'
                  ' this is not recommended.')

        # Continue initialization...
        super().__init__(*args, **kwargs)

    def do_GET(self):
        '''
        GET requests are used for webhook verifications.
        '''
        response = ''
        try:
            # When verification request is sent, it's checked in the internal function,
            # If the internal function didn't raise any 'InvalidVerifyRequest',
            # then return an 200 "OK" response with the challenge content.
            response = self._handle_verify_request()
            self.send_response(http.client.OK)
        except Exception as e:
            # If exception is raised, return 400 "Not Found" response.
            self.send_error(http.client.NOT_FOUND)

            # If the exception is not 'InvalidVerifyRequest', re-raise it.
            # Only 'InvalidVerifyRequest' exceptions shouldn't be re-raised.
            if e is not InvalidVerifyRequest:
                raise e
        finally:
            # End headers to complete request.
            self.end_headers()
            self.wfile.write(response.encode())

    def do_POST(self):
        '''
        POST requests are used to receive notification. 
        '''
        payload = self._get_post_data()
        sha256_signature = self.headers.get('X-Hub-Signature-256')

        try:
            # Validate payload (https://developers.facebook.com/docs/graph-api/webhooks/getting-started#event-notifications)
            if self.__app_secret is not None and not self._is_valid_payload(payload, sha256_signature):
                raise InvalidPayloadSignature()

            # Send payload to the bot's internal function that handles notifications.
            self.__bot._handle_notification(payload)
        except Exception as e:
            # TODO:
            #   1. Implement a callback for failed notifications (?)
            #       A good idea would be to store the information about the failed notification with a random identifier,
            #       and send the contact a template message containing the identifier to send it to the support team.
            #   2. Store failed notifications to analyze them later (?)

            # For now, print to console when an exception is raised.
            print(f'[!] Exception raised: {e}')

            # TODO: After calling the failed notification callback,
            #       this should re-raise the exception if it's not a parsing exception.
        finally:
            # TODO: Define an exception for parsing errors, when it occurs,
            #       print a message about the process of reporting the error to repository GitHub issues.
            #       (It's probably a good idea to ask for the notification payload, after manually removing sensitive information)

            # A 200 'OK' response will always be sent back.
            # if not, Facebook's Graph-API will resend the notification immediately,
            # then try a few more times with decreasing frequency over the next 36 hours.
            #
            # This avoids the event of deduplication of notifications,
            # which will (probably) result with the same exception, depends on the cause of the exception.
            self.send_response(http.client.OK)
            self.end_headers()

    def _get_post_data(self) -> bytes:
        # Read the data from the read-file.
        # The length of the data is provided in the 'Content-Length' header.
        return self.rfile.read(int(self.headers['Content-Length']))

    def _handle_verify_request(self) -> str:
        '''
        Validates the incoming verification request.

        Returns the challenge to reply on success.

        Raises 'InvalidVerifyRequest' on invalid request.

        According to:
        https://developers.facebook.com/docs/graph-api/webhooks/getting-started#verification-requests
        '''

        # Make sure the requested path is the verify endpoint.
        if (parsed_url := urllib.parse.urlparse(self.path)).path != self.__webhook_path:
            raise InvalidVerifyRequest('Requested path is not verify endpoint.'
                                       f' (requested path: "{parsed_url.path}", webhook path: "{self.__webhook_path}" )')

        # Make sure each query parameter has only one value.
        try:
            query_components = self._parse_query_string(parsed_url.query)
        except ValueError:
            # raised in 'urllib.parse.parse_qs()' when there are multiple values for a query parameter.
            raise InvalidVerifyRequest('A query parameter has more than one value.'
                                       f' (query parameters: {parsed_url.query})')

        # Check that all required query components are present.
        if not {'hub.mode', 'hub.challenge', 'hub.verify_token'} <= {*(query_components)}:
            raise InvalidVerifyRequest('Not all required parameters are present.'
                                       f' (parameters: "{set(query_components)}")')

        # 'hub.mode' should always be set 'subscribe'.
        if query_components['hub.mode'] != 'subscribe':
            raise InvalidVerifyRequest('The "hub.mode" parameter is not set to "subscribe".'
                                       f' (hub.mode: "{query_components["hub.mode"]}")')

        # the 'hub.verify_token' must be equal to the verify token.
        if query_components['hub.verify_token'] != self.__verify_token:
            raise InvalidVerifyRequest('The "hub.verify_token" is not equal to the secret verify token.'
                                       f' (hub.verify_token: "{query_components["hub.verify_token"]}")')

        # Send a response containing the challenge.
        return query_components['hub.challenge']

    def _parse_query_string(self, query) -> Dict[str, str]:
        # urllib.parse.parse_qs() returns a dictionary of query parameters paired with a list of values.
        # this function makes sure there is only 1 value for each parameter and returns the dictionary with
        # the same keys, and values as the data itself and not as a list.
        parsed_result = {}

        for name, value in urllib.parse.parse_qsl(query):
            if name in parsed_result:
                raise ValueError('A query parameter has more than one value.')

            parsed_result[name] = value

        return parsed_result

    def _is_valid_payload(self, payload: bytes, sha256_signature: Optional[str]) -> bool:
        """
        Takes the raw payload, encodes it to be unicode escaped,
        calculates the sha256 of it, and compares it against the given sha256.

        returns whether the given sha256 is equal to the calculated one. 
        """
        # If the given sha256 is None, the payload is invalid.
        if sha256_signature is None or not sha256_signature.startswith('sha256='):
            return False

        # Calculate payload sha256 digest.
        digest = hmac.new(self.__app_secret.encode(),
                          payload, hashlib.sha256).hexdigest()

        # Return digests compare result.
        return hmac.compare_digest(sha256_signature, f'sha256={digest}')


class BaseWhatsAppBot(abc.ABC):
    '''
    Base WhatsApp bot.

    This is an abstract class for implementing WhatsApp bots with wacpy.

    [TODO] Add examples.
    '''

    GRAPH_API_HOST = 'graph.facebook.com'

    def __init__(self, phone_id, access_token):
        # Initializing a bot requires only the parameters that are required for sending a message.
        # To receive messages, see 'activate_webhook' method.
        self.__phone_id = phone_id
        self.__access_token = access_token

    def send_message(self, message: Message) -> Dict[str, Any]:
        (connection := http.client.HTTPSConnection(self.GRAPH_API_HOST)).request(
            'POST',
            url=f'/v{WA_CLOUD_API_COMPATIBILITY}/{self.__phone_id}/messages',
            body=message.to_json(),
            headers=self.__authorization | {
                # The sent content is JSON.
                'Content-Type': 'application/json',
                # Signal that the connection will be closed after completion of the response.
                'Connection': 'close'
            }
        )
        # Decide what to do according to the response status.
        match (response := connection.getresponse()).status:
            case http.client.OK:
                # Parse the response as json if the return code is 200 OK.
                return json.loads(response.read().decode())

            case http.client.UNAUTHORIZED:
                # This means the Bearer token is invalid.
                raise InvalidBearerToken('Bearer token is invalid.')

            # TODO: Any other responses to handle?

            case _:
                # Safeguard that will raise a generic exception about unexpected response codes.
                # It's worth reporting this exception in the GitHub issues, as it may be possible to handle the unexpected response code.
                # https://github.com/Natanel-Shitrit/wacpy/issues
                raise BaseWhatsAppBotError(f'Unexpected response code {response.status},'
                                           'please report at https://github.com/Natanel-Shitrit/wacpy/issues.')

    def activate_webhook(self, bind_address, port, request_handler=BasicWhatsAppRequestHandler, **kwargs):
        # Extra request handler parameters are passed via kwargs.
        # The default request handler is 'BasicWhatsAppRequestHandler'.
        # See 'BasicWhatsAppRequestHandler.__init__()' for required parameters.
        request_handler = functools.partial(
            request_handler,
            self,
            **kwargs
        )

        # Initialize http server and start it immediately.
        with http.server.ThreadingHTTPServer((bind_address, port), request_handler) as httpd:
            httpd.serve_forever()

    '''
    Callbacks
    '''
    @abc.abstractmethod
    def on_notification(self, notification: Notification):
        pass

    '''
    Properties
    '''
    @property
    def __authorization(self) -> Dict[str, str]:
        return {'Authorization': f'Bearer {self.__access_token}'}

    '''
    Internal functions
    '''

    def _handle_notification(self, payload):
        # This method could be overridden to allow modification or usage of the raw payload.
        self.on_notification(
            notification=Notification.from_json(payload)
        )


class BaseWhatsAppBotError(Exception):
    '''A base class for wacpy bot exceptions'''


class InvalidBearerToken(BaseWhatsAppBotError):
    '''Raised when Bearer token is invalid'''


class InvalidVerifyRequest(BaseWhatsAppBotError):
    '''Raised when verify request is invalid'''


class InvalidPayloadSignature(BaseWhatsAppBotError):
    '''Raised when the provided payload signature doesn't match the calculated signature'''
