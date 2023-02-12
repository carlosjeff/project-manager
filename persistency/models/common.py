from tortoise import Model, fields
from enum import Enum


class StatusOptions(int, Enum):
    Active = 1
    Disabled = 2


class RoleOptions(str, Enum):
    Default = "default"
    Admin = "admin"


class CommonModel:
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)
    deleted_at = fields.DatetimeField(null=True)
    status = fields.IntField()