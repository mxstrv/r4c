from django.core.mail import send_mail
from django.conf import settings


def send_order_emails(model, version, mail_list):
    """
   Функция отправляет электронные письма клиентам, которые находятся
   в листе ожидания.

   :param model: Название модели товара.
   :type model: str
   :param version: Версия товара.
   :type version: str
   :param mail_list: Список адресов электронной почты, на которые будет отправлено уведомление.
   :type mail_list: list
   :return: None
    """
    message_text = f'Добрый день!\n' \
                   f'Недавно вы интересовались ' \
                   f'нашим роботом модели {model}, версии {version}.\n' \
                   'Этот робот теперь в наличии. Если вам подходит' \
                   ' этот вариант - пожалуйста, свяжитесь с нами'

    send_mail(
        subject='Робот в наличии',
        message=message_text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=mail_list,
        fail_silently=False
    )
