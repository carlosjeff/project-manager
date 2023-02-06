from utils.customizations.route_table_custom import RouteTableCustom
from persistency.models.member import Member
from logic.member_services import MemberServces
from aiohttp import web

member_route = RouteTableCustom("/member")


class MemberRoute:

    @member_route.get('/')
    async def ger_all(self):
        member = await MemberServces().get_all()
        return web.json_response(member)

