from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from core.dataclasses.user_dataclass import User
from core.enums.action_token_enum import ActionTokenEnum
from core.exceptions.jwt_exception import JWTException

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

UserModel: User = get_user_model()


class ActionToken(BlacklistMixin, Token):
    pass


ActionTokenClassType = Type[BlacklistMixin | Token]


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime


class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def verify_token(token, token_class: ActionTokenClassType):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except Exception:
            raise JWTException
        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)