from datetime import datetime


def validate_robot_creation(data: dict) -> tuple[bool, dict]:
    """
    Функция валидирует данные о роботе, передаваемые на вход.

    :param data: Словарь с данными о роботе, включающий в себя модель, версию и дату создания.
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

    if len(data['model']) > 2 or len(data['version']) > 2:
        return False, {'error': 'model and/or version should be 2 characters max.'}

    date_required_format = '%Y-%m-%d %H:%M:%S'
    try:
        datetime.strptime(data['created'], date_required_format)
    except ValueError:
        return False, {'error': "Incorrect data format, should be YYYY-MM-DD HH:MM:SS"}

    return True, data
