import json

from utils.customizations.route_table_custom import RouteTableCustom
from persistency.schemas.member_schemas import MemberModel, DtoCreateMember
from logic.member_services import MemberServices
from aiohttp import web
from utils.middlewares.route_controller import Get, Post, Patch, Delete
from utils.middlewares.protect_route import Protect

member_route = RouteTableCustom("/member")


class MemberRoute:

    @Get(
        route=member_route,
        path='/',
        status_code=200
    )
    async def get_all(request):
        members = await MemberServices().get_all()
        return web.json_response([MemberModel(member).json() for member in members])

    @Get(
        route=member_route,
        path='/{member_id}',
        status_code=200
    )
    @Protect("admin")
    async def get_one(request, member_id: int):
        member = await MemberServices().get_by_id(member_id)
        return web.json_response(member)

    @Post(
        route=member_route,
        path="/",
        status_code=201
    )
    async def create(request, member_input):
        dto_member = DtoCreateMember(member_input)
        member = await MemberServices().create(dto_member)
        return web.json_response(member)

    @Patch(
        route=member_route,
        path="/{id}",
        status_code=204
    )
    @Protect("admin")
    async def update(request, id: int, member_input):
        await MemberServices().update(id, member_input)
        return web.HTTPNoContent()

    @Delete(
        route=member_route,
        path="/{id}",
        status_code=204
    )
    @Protect("admin")
    async def delete(request, id):
        await MemberServices().delete(id)
        return web.HTTPNoContent()

