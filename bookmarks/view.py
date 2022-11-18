from flask import Blueprint, redirect, render_template

from utils import get_post_by_pk, add_bookmark, remove_bookmark, get_bookmark_json

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


# Представление добавления закладки
@bookmarks_blueprint.route('/bookmarks/add/<int:postid>')
def add_bookmark_page(postid):
    add_bookmark(postid)
    return redirect("/", code=302)


# Представление удаления закладки
@bookmarks_blueprint.route('/bookmarks/remove/<int:postid>')
def remove_bookmark_page(postid):
    remove_bookmark(postid)
    return redirect("/", code=302)


# Вывод всех закладок
@bookmarks_blueprint.route('/bookmarks')
def get_bookmark_page():
    bookmarks = get_bookmark_json()
    return render_template('bookmarks.html', bookmarks=bookmarks)
