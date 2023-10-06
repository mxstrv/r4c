from django.core.mail import send_mail
from django.conf import settings


def send_order_emails(model, version, maillist):
    message_text = f'Добрый день!\n' \
                   f'Недавно вы интересовались ' \
                   f'нашим роботом модели {model}, версии {version}.\n' \
                   'Этот робот теперь в наличии. Если вам подходит' \
                   ' этот вариант - пожалуйста, свяжитесь с нами'

    send_mail(
        subject='Робот в наличии',
        message=message_text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=maillist,
        fail_silently=False
    )
