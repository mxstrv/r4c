import re


def validate_order(data: dict) -> tuple[bool, dict]:
    """
    Функция валидирует данные о заказе.

    :param data: Словарь с данными о заказе, включающий в себя
    электронную почту клиента и необходимую модель робота.
    :type data: dict
    :return: Кортеж, первый элемент которого является булевым значением,
             указывающим на успешность валидации,а второй элемент - словарем с
             данными в случае успеха или сообщением об ошибке в случае неудачи.
    :rtype: tuple[bool, dict]
    """
    fields = ('customer', 'robot_serial')

    for field in fields:
        if not data.get(field):
            return False, {'error': f'{field} is missing.'}

    data = {key: data[key] for key in fields}

    regex_serial_pattern = r"^[A-Z0-9]{2}-[A-Z0-9]{2}$"
    regex_email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex_serial_pattern, data['robot_serial']):
        return False, {'error': 'wrong serial number format'}
    if not re.match(regex_email_pattern, data['customer']):
        return False, {'error': 'invalid e-mail'}
    return True, data
