from utils.validators.member_validator import (
    MemberValidatorCreate,
    MemberValidatorUpdate
)
from persistency.models.member import Member

class DtoCreateMember(MemberValidatorCreate):
    def __init__(self, member):
        super().__init__(member)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def response(self):
        return {
            "name": self._name,
            "email": self._email,
            "password": self._password
        }

class DtoUpdateMember(MemberValidatorUpdate):
    def __init__(self, member):
        super().__init__(member)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def response(self):
        return {
            "name": self._name
        }

class MemberModel:
    def __init__(self, member: Member):
        self._id = member.id
        self._name = member.name
        self._email = member.email
        self._created_at = member.created_at
        self._status = member.status
        self._role = member.role

    def json(self):

        return {
            "id": self._id,
            "name": self._name,
            "email": self._email,
            "created_at": str(self._created_at),
            "status": self._status,
            "role": self._role
        }

