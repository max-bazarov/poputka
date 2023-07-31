import smtplib
from email.message import EmailMessage
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from pydantic import EmailStr

from app.auth.config import config
from app.auth.jwt import create_access_token

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent.parent / 'templates')
)


async def create_email(user_email: str, user_name: str, user_id: int):
    token = await create_access_token(user_id=user_id)
    body = {'name': user_name, 'token': token}

    template = env.get_template('email_verif.html')
    rendered_content = template.render(**body)

    email = EmailMessage()
    email['Subject'] = 'Подтверждение почты'
    email['From'] = f'{config.MAIL_FROM_NAME} <{config.MAIL_FROM}>'
    email['To'] = user_email
    email.set_content(rendered_content, subtype='html')

    return email


async def send_email(user_email: EmailStr, user_name: str, user_id: int):
    email = await create_email(
        user_email=user_email, user_name=user_name, user_id=user_id
    )

    with smtplib.SMTP_SSL(config.MAIL_SERVER, config.MAIL_PORT) as server:
        server.login(config.MAIL_USERNAME, config.MAIL_PASSWORD)
        server.send_message(email)
