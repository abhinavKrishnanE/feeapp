from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = "Send emails"

    def handle(self, *args, **kwargs):
        subject = "Sample mail"
        message = "Hello how are you"
        from_email = settings.EMAIL_HOST_USER
        recipient_email = ["abhikrishe@gmail.com"]

        send_mail(subject, message, from_email, recipient_email)