from utils.customizations.route_table_custom import RouteTableCustom
from utils.middlewares.route_controller import Post, Get
from persistency.schemas.login_schemas import LoginModel
from aiohttp.web import json_response, HTTPFound
from logic.login_services import LoginServices
from utils.providers.google_calendar_providers import GoogleCalendarProviders
from aiohttp.web import HTTPFound

login_route = RouteTableCustom("/login")

class LoginRoute:

    @Post(
        route=login_route,
        path="/",
        status_code=200
    )
    async def login(request, login_input):
        login = LoginModel(login_input)
        token = await LoginServices.login(login)
        return json_response(token)

    @Get(
        route=login_route,
        path="/google-login/",
    )
    async def google_login(request):
        return GoogleCalendarProviders.authorization_url()

    @Get(
        route=login_route,
        path="/google/",
    )
    async def google_callback(request):
        code = request.query.get('code')

        #RECEBER TOKEN DA TABELA CREDECIAIS E VALIDAR SE O TOKEN JA ESPIROU
        token = None

        if not token:
            if not code:
                return HTTPFound('/login/google-login/')
            token = GoogleCalendarProviders.get_token(code)

        events = GoogleCalendarProviders.get_calendar(token)


        return json_response(events)