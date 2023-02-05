from tortoise import Model, fields


class CommonModel:
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)
    deleted_at = fields.DatetimeField(null=True)
    status = fields.IntField()