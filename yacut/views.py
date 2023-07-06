from flask import redirect, render_template, flash

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id, check_short_id


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
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)
