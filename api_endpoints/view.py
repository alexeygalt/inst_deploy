from flask import Flask, Blueprint, jsonify, request
import logging

from utils import get_posts_all, get_post_by_pk

# я конечно почитал, и понял что по хорошему это реализуется совершенно не так ( но нам это пока рановато)
api_blueprint = Blueprint('api_blueprint', __name__)


# список всех постов по api/posts
@api_blueprint.route('/api/posts')
def get_api_posts():
    logging.info('Запрос к списку постов')
    result = get_posts_all()
    return jsonify(result)


# получение поста   по /api/posts/<int:post_id>
@api_blueprint.route('/api/posts/<int:post_id>')
def get_api_post(post_id):
    logging.info(f'Запрос к посту {post_id}')
    result = get_post_by_pk(post_id)
    return jsonify(result)
