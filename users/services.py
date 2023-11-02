from django.conf import settings
from django.core.mail import send_mail


def _send_mail_email(recipient_list):
    send_mail(
        subject='Подтверждение почты',
        message=f'Подтвердите вашу почту и перейдите по ссылке http://127.0.0.1:8000/users/verification/{id}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_list]
    )

def _send_mail_password(new_password, recipient_list):
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль{new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_list]
    )