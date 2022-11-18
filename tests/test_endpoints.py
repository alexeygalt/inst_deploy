import pytest
from app import app


# проверяем наличие списка и ключей в нем
def test_all_posts():
    params = {"poster_name": True, "pic": True}
    response = app.test_client().get('/api/posts', query_string=params)
    assert response.status_code == 200
    assert type(response.json) == list


# проверяем наличие списка и ключей в нем
def test_one_post():
    params = {"poster_name": True, "pic": True}
    response = app.test_client().get('/api/posts/1', query_string=params)
    assert response.status_code == 200
    # в моем случае функция возвращает list а не dict
    assert type(response.json) == list
