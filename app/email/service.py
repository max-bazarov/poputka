from email.message import EmailMessage
from pathlib import Path

from celery.exceptions import CeleryError
from jinja2 import Environment, FileSystemLoader

from app.email.config import email_settings
from app.email.schemas import UserRegisterEmailSchema
from app.logger import logger
from app.tasks.tasks import create_sending_email_task

env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))


class EmailService:
    @staticmethod
    def _create_email(email_data: UserRegisterEmailSchema):
        body = {
            "name": email_data.user_name,
            "access_token": email_data.user_access_token,
        }

        template = env.get_template("email_verif.html")
        rendered_content = template.render(**body)

        email = EmailMessage()
        email["Subject"] = email_data.subject
        email["From"] = f"{email_settings.MAIL_FROM_NAME} <{email_settings.MAIL_FROM}>"
        email["To"] = email_data.user_email
        email.set_content(rendered_content, subtype="html")

        return email

    @staticmethod
    def send_email(email_data: UserRegisterEmailSchema):
        email = EmailService._create_email(email_data)

        try:
            create_sending_email_task(email)
            extra = {**email_data.model_dump()}
            logger.info("Email task was created", extra=extra)

        except (CeleryError, Exception) as e:
            if isinstance(e, CeleryError):
                msg = "Celery Exc: Cannot create task"
            elif isinstance(e, Exception):
                msg = "Uknown Exc: Cannot create task"

            extra = {**email_data.model_dump()}
            logger.error(msg, extra=extra, exc_info=True)
