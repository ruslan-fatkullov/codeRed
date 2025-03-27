from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, FileField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    service_type = SelectField('Тип услуги', choices=[
        (0, 'Веб-сервисы'),
        (1, 'Дизайн'),
        (2, 'Продвижение'),
        (3, 'Разроботка ПО'),
        (4, 'Сервисные услуги')

    ], validators=[DataRequired()])  # Новое поле: тип услуги
    description = TextAreaField('Описание услуги', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    development_time = StringField('Время разработки', validators=[DataRequired()])
    route = StringField('Маршрут ссылки на страницу', validators=[DataRequired()])
    image = FileField('Большое изображение', id="serviceImageForm", validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'svg', 'webp'], 'Только изображения!')  # Разрешенные форматы
    ])
    icon = FileField('Иконка услуги', id="serviceIconForm", validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'svg', 'webp'], 'Только изображения!')  # Разрешенные форматы
    ])
    published = BooleanField('Опубликована')
    submit = SubmitField('Добавить услугу')
