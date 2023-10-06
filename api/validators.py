import re
from datetime import datetime


def validate_robot_creation(data: dict) -> tuple[bool, dict]:
    """
    Функция валидирует данные о роботе, передаваемые на вход.
    Валидация модели и версии идет с использованием регулярных выражений.

    :param data: Словарь с данными о роботе,
            включающий в себя модель, версию и дату создания.
    :type data: dict
    :return: Кортеж, первый элемент которого является булевым значением,
             указывающим на успешность валидации,а второй элемент - словарем с
             данными в случае успеха или сообщением об ошибке в случае неудачи.
    :rtype: tuple[bool, dict]
    """
    fields = ('model', 'version', 'created')

    for field in fields:
        if not data.get(field):
            return False, {'error': f'{field} is missing.'}

    data = {key: data[key] for key in fields}

    regex_pattern = r"^[A-Z0-9]{2}$"

    if (not re.match(regex_pattern, data['model'])
            or not re.match(regex_pattern, data['version'])):
        return False, {
            'error': 'model and/or version should be 2 characters max.'}

    date_required_format = '%Y-%m-%d %H:%M:%S'
    try:
        datetime.strptime(data['created'], date_required_format)
    except ValueError:
        return False, {'error': "data format should be YYYY-MM-DD HH:MM:SS"}

    return True, data
