from app.core.service import BaseService
from app.users.models import User


class UserService(BaseService):
    model = User
