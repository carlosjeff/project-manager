import json

from utils.middlewares.session_controller import SessionDB
from persistency.models.member import Member, DtoCreateMember, MemberModel
from datetime import datetime
from persistency.models.common import StatusOptions, RoleOptions
from utils.exceptions.http_exceptions import BadRequest, NotFound
from utils.providers.hash_provider import Hash

class MemberServices:

    @staticmethod
    @SessionDB
    async def get_all():
        member = await Member.filter(
            status=StatusOptions.Active).all()
        return member

    @staticmethod
    @SessionDB
    async def get_by_id(member_id: int):
        try:
            member = await Member.get(
                id=member_id,
                status=StatusOptions.Active)
            return MemberModel(member).json()
        except:
            raise NotFound('the member does not exist')

    @staticmethod
    @SessionDB
    async def get_by_email(member_email: str):
        try:
            member = await Member.get(
                email=member_email,
                status=StatusOptions.Active)
            return member
        except:
            raise NotFound('the member does not exist')

    @staticmethod
    @SessionDB
    async def email_exist(member_email: str):
        member = await Member.exists(
            email=member_email)
        return member

    @staticmethod
    @SessionDB
    async def create(member: DtoCreateMember):
        email_exist = await MemberServices.email_exist(member.email)
        if email_exist:
            raise BadRequest(f"Email {member.email} already exists")

        member_new = await Member.create(
            name=member.name,
            email=member.email,
            password=Hash.generate(member.password),
            status=StatusOptions.Active,
            role= RoleOptions.Default
        )
        return MemberModel(member_new).json()

    @staticmethod
    @SessionDB
    async def update(member_id, member):
        member["updated_at"] = datetime.now()
        await Member.filter(
            id=member_id,
            status=StatusOptions.Active).update(**member)

    @staticmethod
    async def delete (member_id):
       await MemberServices.update(
           member_id,
           {
               "status": StatusOptions.Disabled,
               "deleted_at": datetime.now()
           })

