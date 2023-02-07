from tortoise import fields, Model
from persistency.models.common import CommonModel
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class Member(CommonModel,Model):
    name = fields.CharField(100)
    email = fields.CharField(100, unique=True)
    password = fields.CharField(255)

    def __str__(self):
        return f"Member {self.id}: {self.name}"


class MemberOutput(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True