from utils.customizations.route_table_custom import RouteTableCustom
from utils.middlewares.route_controller import Post
from persistency.models.member import LoginModel
from aiohttp.web import json_response
from logic.login_services import LoginServices

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