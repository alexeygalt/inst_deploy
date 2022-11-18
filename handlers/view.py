from flask import Blueprint, render_template

handlers_blueprint = Blueprint('handlers_blueprint', __name__, template_folder='templates')


# обработчик запросов к несуществующим страницам
@handlers_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# обработчик ошибок, возникших на стороне сервера
@handlers_blueprint.app_errorhandler(500)
def page_not_found(e):
    return render_template('505.html')
