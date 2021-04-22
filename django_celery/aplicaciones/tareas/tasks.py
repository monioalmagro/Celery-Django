from celery import shared_tasks
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_emails_user():
    asunto = "mensaje de prueba"
    mensaje = "bienvenido este es un mensaje de prueba"
    users = User.objects.all()
    for x in users:
        send_mail(sunto,mensaje)
