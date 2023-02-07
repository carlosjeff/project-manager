from utils.customizations.route_table_custom import RouteTableCustom
from persistency.models.member import Member, MemberOutput
from logic.member_services import MemberServces
from aiohttp import web
import json

member_route = RouteTableCustom("/member")


class MemberRoute:

    @member_route.get('/')
    async def get_all(request):
        members = await MemberServces().get_all()
        return web.json_response([MemberOutput.from_orm(member).dict() for member in members])

    @member_route.get('/{id}')
    async def get_one(request):
        id = request.match_info['id']
        member = await MemberServces().get_by_id(id)
        return web.json_response(MemberOutput.from_orm(member).dict())

    @member_route.post('/')
    async def create(request):
        data_request = await request.json()
        member = await MemberServces().create(data_request)
        return web.json_response(MemberOutput.from_orm(member).dict(), status=201)


    @member_route.patch('/{id}')
    async def update(request):
        data_request = await request.json()
        id = request.match_info['id']
        await MemberServces().update(id, data_request)
        return web.json_response(status=204)

    @member_route.delete('/{id}')
    async def update(request):
        id = request.match_info['id']
        await MemberServces().delete(id)
        return web.json_response(status=204)

