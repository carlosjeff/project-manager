from utils.middlewares.session_controller import SessionDB
from persistency.models.member import Member


class MemberServces:

    @classmethod
    @SessionDB
    async def get_all(cls):
        member = await Member.all()
        return member
