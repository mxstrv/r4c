import re


def validate_order(data: dict):
    fields = ('customer', 'robot_serial')

    for field in fields:
        if not data.get(field):
            return False, {'error': f'{field} is missing.'}

    data = {key: data[key] for key in fields}

    regex_serial_pattern = r"^[A-Z0-9]{2}-[A-Z0-9]{2}$"
    regex_email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex_serial_pattern, data['customer']):
        return False, {'error': 'wrong serial number format'}
    if not re.match(regex_email_pattern, data['customer']):
        return False, {'error': 'invalid e-mail'}
    return True, data
