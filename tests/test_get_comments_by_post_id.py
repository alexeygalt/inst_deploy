import pytest
from utils import get_comments_by_post_id

# тестируем функцию get_comments_by_post_id
get_comments_by_user_par = [1, 4, 2]
get_comments_by_user_exceptions = [('322', TypeError), (32.2, TypeError), (322, ValueError)]


@pytest.mark.parametrize("input_str", get_comments_by_user_par)
def test_get_posts_by_user_par(input_str):
    assert type(get_comments_by_post_id(input_str)) == list


@pytest.mark.parametrize("input_str, exceptions", get_comments_by_user_exceptions)
def test_get_posts_by_user_par_exceptions(input_str, exceptions):
    with pytest.raises(exceptions):
        get_comments_by_post_id(input_str)
