from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    abort,
    flash,
    session,
)
# from routes.base_routes import profile_bp

from settings import settings
# from db_session import global_init, create_session (DB)

import base64

import random

app = Flask(__name__)
settings(app)
app.jinja_env.globals['base64'] = base64
# global_init(app.config['DATABASE_URI']) (DB)

# app.register_blueprint(blog_bp)
# app.register_blueprint(profile_bp)
# app.register_blueprint(project_bp)
# app.register_blueprint(rating_bp)
# app.register_blueprint(forum_bp)


@app.route('/')
def index():
    return render_template('index.html')


data_errors = {
    401: {"text": "Неверный логин или пароль", "tags": ["абоба"]},
    403: {
        "text": "Доступ запрещён (Виктор зарещает)",
        "tags": ["наш слоняра"],
    },
    404: {
        "text": "Ой, ой, ой... Страница не найдена",
        "tags": ["договорничок"],
    },
    405: {
        "text": "Нет такого метода запроса (Виктор не даст вам данные!)",
        "tags": ["авава"],
    },
    418: {
        "text": "Хаха, я чайник (Виктор)",
        "tags": ["авава", "абоба", "договорничок", "наш слоняра"],
    },
    500: {
        "text": "У нас сбой (Виктор вас не наругает, вы не виноваты)",
        "tags": ["наш слоняра"],
    },
    502: {"text": "Проблему у нашего сервера", "tags": ["абоба"]},
    503: {
        "text": "Сервис временно недоступен. Виктор пока чинет сайт, подождите",
        "tags": ["договорничок"],
    },
    504: {
        "text": "Запрос обрабатывается слишком долго. Таймаут, Виктор отключил соединение",
        "tags": ["авава"],
    },
}
def error_handlers(app, errors):
    for code, info in errors.items():

        @app.errorhandler(code)
        def error_handle(_, code=code, info=info):
            return (
                render_template(
                    'error.html',
                    code=code,
                    text=info["text"],
                    tags=info["tags"],
                ),
                code,
            )
error_handlers(app, data_errors)
@app.route('/error/<int:code>')
def error(code):
    if code in data_errors.keys():
        abort(code)
    else:
        flash(f'Ошибка с номером {code} не обрабатывается.', 'danger')
        return redirect('/')


@app.route('/about')
def about():
    return render_template('about.html', have_parallax=False)


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'],
    )
