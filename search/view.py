from flask import Blueprint, render_template, request

from utils import search_for_posts, get_posts_by_user, get_tags_words

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


# представление для поиска по маршруту GET /search/?s=...
@search_blueprint.route('/search')
def search_page():
    key_word = request.args['key']
    result = search_for_posts(key_word)
    return render_template('search.html', result=result)


# представление с выводом постов конкретного пользователя
@search_blueprint.route('/users/<user_name>')
def get_user_page(user_name):
    user_list = get_posts_by_user(user_name)
    return render_template('user-feed.html', user_list=user_list, user_name=user_name)
