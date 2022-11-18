import pytest
from utils import get_posts_by_user

# тестируем функцию get_posts_by_user
get_posts_by_user_par = ['hank', 'leo', 'johnny']
get_posts_by_user_exceptions = [(322, TypeError), (32.2, TypeError), ('Alex', ValueError)]


@pytest.mark.parametrize("input_str", get_posts_by_user_par)
def test_get_posts_by_user_par(input_str):
    assert type(get_posts_by_user(input_str)) == list


@pytest.mark.parametrize("input_str, exceptions", get_posts_by_user_exceptions)
def test_get_posts_by_user_par_exceptions(input_str, exceptions):
    with pytest.raises(exceptions):
        get_posts_by_user(input_str)
