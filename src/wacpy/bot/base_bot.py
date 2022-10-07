import http.client
import http.server
import urllib.parse
import json
from abc import ABCMeta, abstractmethod
from typing import Any, Dict

from wacpy.types.notification.notification import Notification

from .. import WA_CLOUD_API_COMPATIBILITY, types


class BaseWhatsAppBot(http.server.BaseHTTPRequestHandler, metaclass=ABCMeta):
    '''
    Base WhatsApp bot.

    This is an abstract class for implementing WhatsApp bots with wacpy.

    [TODO] Add examples.
    '''

    GRAPH_API_HOST = 'graph.facebook.com'

    def __init__(self, phone_id, access_token, verify_token, verify_endpoint='/', *args, **kwargs):
        # Connection to facebook graph api, to send messages.
        self.__graph_api = http.client.HTTPSConnection(self.GRAPH_API_HOST)

        # Parameters.
        self.__phone_id = phone_id
        self.__access_token = access_token
        self.__verify_token = verify_token
        self.__verify_endpoint = verify_endpoint

        # Initialize HTTP request handler.
        super().__init__(*args, **kwargs)

    def send_message(self, message: types.Message) -> Dict[str, Any]:
        self.__graph_api.request(
            'POST',
            url=f'/{self.__phone_id}/messages',
            body=message.to_dict(),  # type: ignore
            headers=self.__authorization | {'Content-Type': 'application/json'}
        )

        match (response := self.__graph_api.getresponse()).status:
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
                raise BaseWhatsAppBotError(
                    f'Unexpected response code {response.status}.')

    '''
    HTTP server methods handlers.
    '''

    def do_GET(self):
        '''
        GET requests are used for webhook verifications.
        '''
        try:
            # When verification request is sent, it's checked in the internal function,
            # If the internal function didn't raise any 'InvalidVerifyRequest',
            # then return an 200 "OK" response with the challenge content.
            self.send_response(
                http.client.OK,
                self.__get_verify_request_challenge()
            )
        except InvalidVerifyRequest:
            # If 'InvalidVerifyRequest' is raised, return 400 "Not Found" response.
            self.send_error(http.client.NOT_FOUND)

    def do_POST(self):
        '''
        POST requests are used to receive notification. 
        '''
        try:
            # Get data and send it to the internal function that handles notifications.
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            self.__handle_notification(payload=data)
        except:
            # TODO:
            #   1. Implement a callback for failed notifications (?)
            #   2. Store failed notifications to analyze them later (?)
            pass

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

    '''
    Callbacks
    '''
    @abstractmethod
    def on_notification(self, notification: types.Notification):
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

    def __get_verify_request_challenge(self) -> str:
        '''
        Graph-API endpoint for Verification Requests.
        https://developers.facebook.com/docs/graph-api/webhooks/getting-started#verification-requests
        '''

        # Make sure the requested path is the verify endpoint.
        if (parsed_url := urllib.parse.urlparse(self.path)).path != self.__verify_endpoint:
            raise InvalidVerifyRequest(
                f'Requested path is not verify endpoint. (path: "{parsed_url.path}")')

        # Check that all required query components are present.
        if not {'hub.mode', 'hub.challenge', 'hub.verify_token'} <= {*(query_components := urllib.parse.parse_qs(parsed_url.query))}:
            raise InvalidVerifyRequest(
                f'Not all required parameters are present. (parameters: "{set(query_components)}")')

        # 'hub.mode' should always be set 'subscribe'.
        if query_components['hub.mode'] != 'subscribe':
            raise InvalidVerifyRequest(
                f'The "hub.mode" parameter is not set to "subscribe". (hub.mode: "{query_components["hub.mode"]}")')

        # the 'hub.verify_token' must be equal to the verify token.
        if query_components['hub.verify_token'] != self.__verify_token:
            raise InvalidVerifyRequest(
                f'The "hub.verify_token" is not equal to the secret verify token. (hub.verify_token: "{query_components["hub.verify_token"]}")')

        # Send a response containing the challenge.
        return query_components['hub.challenge'][0]

    def __handle_notification(self, payload):
        # TODO: Handle notifications, Call 'on_notification' with parsed notification.
        # TODO: Validate payload (https://developers.facebook.com/docs/graph-api/webhooks/getting-started#event-notifications)
        self.on_notification(
            notification=Notification.from_json(payload)  # type: ignore
        )


class BaseWhatsAppBotError(Exception):
    '''A base class for wacpy bot exceptions'''


class InvalidBearerToken(BaseWhatsAppBotError):
    '''Raised when Bearer token is invalid'''


class InvalidVerifyRequest(BaseWhatsAppBotError):
    '''Raised when verify request is invalid'''
