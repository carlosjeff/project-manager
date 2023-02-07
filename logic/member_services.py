from utils.middlewares.session_controller import SessionDB
from persistency.models.member import Member
from datetime import datetime

class MemberServces:

    @classmethod
    @SessionDB
    async def get_all(cls):
        member = await Member.filter(status=1).all()
        return member

    @classmethod
    @SessionDB
    async def get_by_id(cls, id: int):
        member = await Member.get(id=id, status=1)
        return member

    @classmethod
    @SessionDB
    async def create(cls, member: Member):
        member_new = await Member.create(
            name=member["name"],
            email=member["email"],
            password=member["password"],
            status = 1
        )
        return member_new

    @classmethod
    @SessionDB
    async def update(cls,id ,member):
        member["updated_at"] = datetime.now()
        await Member.filter(id=id, status=1).update(**member)

    @classmethod
    async def delete(cls, id):
       await cls.update(id, {"status": 2})