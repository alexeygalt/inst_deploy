import pytest
from utils import search_for_posts

# тестируем функцию search_for_posts
search_for_posts_param = ['погулять', 'Квадратная', 'красивый']
search_for_posts_exceptions = [(322, TypeError), (3.22, TypeError), (True, TypeError)]


@pytest.mark.parametrize("input_str", search_for_posts_param)
def test_search_for_posts_param(input_str):
    assert type(search_for_posts(input_str)) == list


@pytest.mark.parametrize('input_str, exceptions', search_for_posts_exceptions)
def test_search_for_posts_exceptions(input_str, exceptions):
    with pytest.raises(exceptions):
        search_for_posts(input_str)
