from tortoise import fields, Model
from persistency.models.common import CommonModel
from persistency.models.item import Item

class Collection(CommonModel, Model):
    title = fields.CharField(100)
    description = fields.TextField(null=True)
    origen = fields.IntField()

    members = fields.ManyToManyField("models.Member",
                                     related_name="members")
    items = fields.ForeignKeyRelation[Item]
