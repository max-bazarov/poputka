from app.exceptions import BadRequestException


class EmailTakenException(BadRequestException):
    DETAIL = 'Email is already taken'
