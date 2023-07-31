import re

STRONG_PASSWORD_PATTERN = re.compile(
    r'^(?=.*[\d])(?=.*[!@#$%^&*-])[\w!@#$%^&*-]{8,24}$'
)

PHONE_NUMBER_PATTERN = re.compile(
    r'^(?:\+7|8)?[-(]?\d{3}[-)]?\d{3}[-]?\d{2}[-]?\d{2}$'
)

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_email(email: str) -> None:
    if not re.match(EMAIL_PATTERN, email):
        raise ValueError('Неверный формат почты')


def validate_password(password: str) -> None:
    if not re.match(STRONG_PASSWORD_PATTERN, password):
        raise ValueError(
            'Пароль должен содержать как минимум'
            'одну маленькую букву, '
            'одну большую букву, '
            'цифру или '
            'специальный символ'
        )


def validate_phone_number(phone_number: str) -> None:
    if not re.match(PHONE_NUMBER_PATTERN, phone_number):
        raise ValueError(
            'Номер телефона недействителен. '
            'Введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX.'
        )
