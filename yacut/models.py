from datetime import datetime

from flask import url_for
from yacut import db


class URLMap(db.Model):
    """Класс модели юрлмап."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Преобразование объекта в словарь."""
        return dict(
            url=self.original,
            short_link=url_for('url_view', short=self.short, _external=True),
        )

    def from_dict(self, data):
        """Преобразование словаря в объект."""
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
