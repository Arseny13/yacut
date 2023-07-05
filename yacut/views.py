from random import choice
import string
import re

from flask import redirect, render_template, flash, abort

from . import app, db
from .forms import URLMapForm
from .models import URLMap

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


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Вьюха главной страницы."""
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('urlmap.html', form=form)
    original = form.original_link.data
    short = form.custom_id.data
    if URLMap.query.filter_by(short=short).first() is not None:
        flash(f"Имя {short} уже занято!")
        return render_template('urlmap.html', form=form)
    if short == '' or short is None:
        short = get_unique_short_id()
    if not check_short_id(short):
        flash(f"{short} не корректна!")
        return render_template('urlmap.html', form=form)
    urlmap = URLMap(
        original=original,
        short=short,
    )
    db.session.add(urlmap)
    db.session.commit()
    return render_template('urlmap.html', form=form, short_url=urlmap.short)



@app.route('/<string:short>', methods=['GET'])
def url_view(short):
    """Вьюха перенапрвление короткой ссылки на оригинальную."""
    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap is not None:
        return redirect(urlmap.original)
    abort(404)