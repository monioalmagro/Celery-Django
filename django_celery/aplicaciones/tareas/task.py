from celery import shared_tasks
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_emails_users():
    asunto = 'Mensaje de prueba'
    mensaje = ' Esto es un mensaje de pruedba Celery '
    users = User.objects.all()
    for x in users:
        send_mail(asunto, mensaje)