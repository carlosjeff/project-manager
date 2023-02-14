

class LoginModel:
    def __init__(self, login):
        self._email = login.get('email')
        self._password = login.get('password')

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @email.setter
    def email(self, value):
        self._email = value

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def json(self):
        return {
            "email": self._email,
            "password": self._password
        }