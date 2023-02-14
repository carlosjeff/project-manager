from aiohttp.web import HTTPFound
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from config import Config
import json

class GoogleCalendarProviders:

    @staticmethod
    def generate_flow_credentials(state=None):
        flow = Flow.from_client_config(
            client_config=dict(
                web=dict(
                    client_id=Config.GOOGLE_CLIENT_ID,
                    project_id=Config.GOOGLE_PROJECT_ID,
                    auth_uri=Config.GOOGLE_AUTH_URI,
                    token_uri=Config.GOOGLE_TOKEN_URI,
                    auth_provider_x509_cert_url=Config.GOOGLE_AUTH_PROVIDER_URL,
                    client_secret=Config.GOOGLE_CLIENT_SECRET,
                    redirect_uris=[Config.GOOGLE_REDIRECT_URI],
                )
            ),
            scopes=[Config.GOOGLE_SCOPE],
            redirect_uri=Config.GOOGLE_REDIRECT_URI,
            state=state,
        )
        return flow

    @staticmethod
    def authorization_url():
        authorization_url, state = (GoogleCalendarProviders
            .generate_flow_credentials()
            .authorization_url(
                prompt="consent"
        ))
        response = HTTPFound(authorization_url)
        response.set_cookie("google_login_state", state)
        return response

    @staticmethod
    def get_token(code: str):
        flow = GoogleCalendarProviders.generate_flow_credentials()
        flow.fetch_token(code=code)
        session = flow.authorized_session()
        return json.loads(session.credentials.to_json())

    @staticmethod
    def get_calendar(token: dict):
        creds = Credentials.from_authorized_user_info(token, Config.GOOGLE_SCOPE)
        service = build('calendar', 'v3', credentials=creds)
        events_result = service.events().list(calendarId='primary',
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        return events_result.get('items', [])



