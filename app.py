from functools import wraps

import flask
from flask_wtf.csrf import CSRFProtect

from src.database.db import init_db
from src.routes.admin import admin
from src.routes.pages import page
from config import Config


def create_app(config_name='default'):
    code_red_application = Flask(__name__)
    code_red_application.config.from_object(Config)
    code_red_application.register_blueprint(page)
    code_red_application.register_blueprint(admin)
    init_db(code_red_application.config.get('DATABASE'))
    csrf = CSRFProtect(code_red_application)
    return code_red_application


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            flash('Пожалуйста, войдите в систему для доступа к этой странице.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True)
