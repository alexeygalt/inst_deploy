from app import app


def test_main_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert "index.html", "Контент страницы неверный"


def test_post_page():
    response = app.test_client().get('/posts/1')
    assert response.status_code == 200
    assert "post.html", "Контент страницы неверный"


def test_search_page():
    params = {'key': "погулять"}
    response = app.test_client().get('/search', query_string=params)
    assert response.status_code == 200
    assert "search.html", "Контент страницы неверный"


def test_users_page():
    response = app.test_client().get('/users/leo')
    assert response.status_code == 200
    assert 'user-feed.html', "Контент страницы неверный"


def test_tag_page():
    response = app.test_client().get('/tag/nature')
    assert response.status_code == 200
    assert 'tag.html', "Контент страницы неверный"


def test_add_bookmark_page():
    response = app.test_client().get('/tag/1')
    assert response.status_code == 200


def test_remove_bookmark_page():
    response = app.test_client().get('/tag/1')
    assert response.status_code == 200
