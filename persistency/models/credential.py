from tortoise import Model, fields
from persistency.models.common import CommonModel


class Credential(CommonModel, Model):
    name = fields.CharField(100)
    credential = fields.TextField()