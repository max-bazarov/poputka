from app.exceptions import BadRequestException, NotAuthenticatedException


class EmailTakenException(BadRequestException):
    DETAIL = 'Пользователь с таким Email уже существует'


class InvalidCredentialsException(NotAuthenticatedException):
    DETAIL = 'Неверно введены данные'


class TokenAbsentException(NotAuthenticatedException):
    DETAIL = 'Токен отсутствует.'


class RefreshTokenNotValid(BadRequestException):
    DETAIL = 'Невалидный refresh токен'
