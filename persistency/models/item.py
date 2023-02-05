from tortoise import fields, Model
from persistency.models.common import CommonModel


class Item(CommonModel, Model):
    title = fields.CharField(100)
    description = fields.TextField(null=True)
    start_date = fields.DatetimeField(null=True)
    end_date = fields.DatetimeField(null=True)
    notify = fields.BooleanField(null=True)

    collection = fields.ForeignKeyField('models.Collection',
                                         related_name="items")
