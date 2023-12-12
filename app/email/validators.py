import re


EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_email(email: str) -> None:
    if not re.match(EMAIL_PATTERN, email):
        raise ValueError("Неверный формат почты")
