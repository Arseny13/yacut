from http import HTTPStatus
from flask import jsonify, request

from yacut import app, db
from yacut.utils import check_short_id, get_unique_short_id
from yacut.models import URLMap
from yacut.error_handlers import InvalidAPIUsage


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_urlmap(short_id):
    """Api для получение оригинатольного юрл."""
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    """Api для создание короткой ссылки."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    original = data['url']
    short = data.get('custom_id', None)
    if not short:
        short = get_unique_short_id()
    if not check_short_id(short):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short).first() is not None:
        raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
    data['original'] = original
    data['short'] = short
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED
