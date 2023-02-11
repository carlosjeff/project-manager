import re
class ValidatorModel:

    def _checks_attribute(self,
                          name: str,
                          type_value,
                          value,
                          required=True,
                          password = False):
        errors = []

        if required and not value:
            errors.append(self._message_error(
                name,
                f"This field {name} is required"
            ))


        if value and type(value) != type_value:
            errors.append(self._message_error(
                name,
                f"the value of field {name} is not of type {type_value}"
            ))

        regex_password = (
            r"^(?=.*[A-Z])(?=.*[!@#$%^&*(\[\])\-_=+])"
            r"(?=.*[0-9])(?=.*[a-z]).{6,20}$"
        )
        if password and not re.match(regex_password, value):
            errors.append(self._message_error(name, (
                f"weak {name}, Must have at least one number, " 
                "one special symbol, one uppercase character, "
                "one lowercase character, and must "
                "be between 6 and 20 characters"
            )))

        return errors

    def _message_error(self,field, error ):
        return {
                "field": field,
                "error": error
            }