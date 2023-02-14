from persistency.schemas.login_schemas import LoginModel
from utils.providers.token_provider import TokenJwt
from utils.providers.hash_provider import Hash
from logic.member_services import MemberServices
from utils.exceptions.http_exceptions import Unauthorized

class LoginServices:

    @staticmethod
    async def login(login: LoginModel):
        member = await MemberServices.get_by_email(login.email)

        if not member or not Hash.verify(login.password, member.password):
            raise Unauthorized('Authenticate failed')

        token = TokenJwt.encoder({"sub": member.id})

        return {"access_token": token}
