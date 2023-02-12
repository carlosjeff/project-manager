from aiohttp.web import AbstractRouteDef, Application, RouteTableDef
from typing import Iterable
from routers.members import member_route
from routers.login import login_route

class RouteManager:
    def __init__(self, app: Application):
        self.app = app
        self.routes: Iterable[AbstractRouteDef] = [member_route, login_route]

    def define_routers(self):
        for route in self.routes:
            self.app.add_routes(route)



