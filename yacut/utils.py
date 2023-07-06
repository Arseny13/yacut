from random import choice
import string
import re

from yacut.models import URLMap

SHORT_MAX_LENGTH = 16


def check_short_id(short):
    """Проверка короткой ссылки."""
    if len(short) > SHORT_MAX_LENGTH:
        return False
    pattern = re.compile(rf'^[{string.ascii_letters + string.digits}]*$')
    return bool(re.search(pattern, short))


def get_unique_short_id():
    """Создание уникально короткой ссылки."""
    while True:
        short = ''.join([choice(string.ascii_letters + string.digits) for _ in range(6)])
        if URLMap.query.filter_by(short=short).first() is None:
            return short