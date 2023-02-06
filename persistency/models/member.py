from tortoise import fields, Model
from persistency.models.common import CommonModel

class Member(CommonModel,Model):
    name = fields.CharField(100)
    email = fields.CharField(100, unique=True)
    password = fields.CharField(255)

