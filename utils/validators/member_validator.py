from utils.validators.validator_model import ValidatorModel
from utils.exceptions.http_exceptions import BadRequest

class MemberValidatorCreate(ValidatorModel):

    def __init__(self, member):
        self._name = member.get("name")
        self._email = member.get("email")
        self._password = member.get('password')

        self._validator = self.validator

        if len(self._validator):
            raise BadRequest('Field error', self._validator)

    @property
    def validator(self):

        errors = [
            *self._checks_attribute("name", str, self._name),
            *self._checks_attribute("email", str, self._email),
            *self._checks_attribute("password", str, self._password,password=True)
        ]

        return errors

class MemberValidatorUpdate(ValidatorModel):

    def __init__(self, member):
        self._name = member["name"]

        self._validator = self.validator

        if len(self._validator):
            raise BadRequest('Field error',self._validator)

    @property
    def validator(self):

        return self._checks_attribute(str, self._name)
