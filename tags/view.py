from flask import Blueprint, render_template

from utils import search_for_tag

tags_blueprint = Blueprint('tags_blueprint', __name__, template_folder='templates')


# представление для вывода всех постов по хэштегу
@tags_blueprint.route('/tag/<tagname>')
def get_tag_page(tagname):
    result = search_for_tag(tagname)
    return render_template('tag.html', result=result, key=tagname)
