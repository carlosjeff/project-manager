import json

from utils.customizations.route_table_custom import RouteTableCustom
import re
import inspect
from aiohttp.web_urldispatcher import UrlMappingMatchInfo
from utils.exceptions.http_exceptions import BadRequest
from aiohttp import web

class RouteRequest:
    def __init__(self, func, path, validators=None, status_code=200):
        self.func = func
        self.path = path
        self.validators = validators
        self.status_code = status_code
        self.params = [name for name, param in inspect.signature(self.func).parameters.items()]

    async def __call__(self, request, *args, **kwargs):
        mapping: UrlMappingMatchInfo = request.match_info
        params = await self.select_body(request)
        for value in re.findall(r"\{(.*?)\}", self.path):
            params.update({value: mapping[value]})
        kwargs.update(params)
        result = await self.func(request, *args, **kwargs)

        return result

    async def select_body(self, request) -> dict:
        try:
            path_params = re.findall(r"\{(.*?)\}", self.path)
            path_params.extend([self.params[0], 'args', 'kwargs'])
            body_param = {}
            for value in self.params:
                if not (value in path_params):
                    body_param[value] = dict(await request.json())
            return body_param
        except json.JSONDecodeError as err:
            raise BadRequest('The JSON syntax is incorrect')


class Get:
    def __init__(self,
                 route: RouteTableCustom,
                 path: str,
                 status_code=200):
        self.route = route
        self.path = path
        self.status_code = status_code

    def __call__(self, func):
        self.route.get(self.path)(RouteRequest(
            func=func,
            path=self.path,
            status_code=self.status_code
        ))


class Post:
    def __init__(self,
                 route: RouteTableCustom,
                 path: str,
                 validators=None,
                 status_code=200):
        self.route = route
        self.path = path
        self.validators = validators
        self.status_code = status_code

    def __call__(self, func):
        self.route.post(self.path)(RouteRequest(
            func=func,
            path=self.path,
            validators=self.validators,
            status_code=self.status_code
        ))

class Patch:
    def __init__(self,
                 route: RouteTableCustom,
                 path: str,
                 validators=None,
                 status_code=200):
        self.route = route
        self.path = path
        self.validators = validators
        self.status_code = status_code

    def __call__(self, func):
        self.route.patch(self.path)(RouteRequest(
            func=func,
            path=self.path,
            validators=self.validators,
            status_code=self.status_code
        ))

class Delete:
    def __init__(self,
                 route: RouteTableCustom,
                 path: str,
                 validators=None,
                 status_code=200):
        self.route = route
        self.path = path
        self.validators = validators
        self.status_code = status_code

    def __call__(self, func):
        self.route.delete(self.path)(RouteRequest(
            func=func,
            path=self.path,
            validators=self.validators,
            status_code=self.status_code
        ))