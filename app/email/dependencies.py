from app.email.service import EmailService


def email_service_factory():
    return EmailService()
