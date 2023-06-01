from django.core.mail import send_mail

def send_mail_to_user(asunto, mensaje, remitente, destinatario):

    send_mail(asunto, mensaje, remitente, destinatario)