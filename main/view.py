from flask import Blueprint, render_template

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_tags_words, get_bookmark_json

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# представление для всех постов
@main_blueprint.route('/')
def get_main_page():
    all_list = get_posts_all()
    bookmarks = get_bookmark_json()

    return render_template('index.html', key=all_list, bookmarks=bookmarks)


# представление для одного поста
@main_blueprint.route('/posts/<int:user_pk>')
def get_post_page(user_pk):
    post_page = get_post_by_pk(user_pk)
    try:
        comments = get_comments_by_post_id(user_pk)
    except ValueError:
        return render_template('post.html', key=post_page)
    key = get_tags_words(post_page)

    return render_template('post.html', key=key, comments=comments)
