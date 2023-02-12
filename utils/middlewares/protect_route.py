from utils.providers.token_provider import TokenJwt
from logic.member_services import MemberServices
from utils.exceptions.http_exceptions import Forbidden


class Protect:
    def __init__(self, level):
        self._level = level

    def __call__(self, function):
        async def wrapper(request, *args, **kwargs):
            token = request.headers.get('Authorization')
            payload = TokenJwt.verify(token)
            member = await MemberServices.get_by_id(payload)
            if not member or member["role"] != self._level:
                raise Forbidden("Not authorized")
            result = await function(request, *args, **kwargs)
            return result

        return wrapper