import pytest
from utils import get_post_by_pk

# тестируем функцию get_post_by_pk
get_post_by_pk_param = [1, 4, 2]
get_post_by_pk_exceptions = [('322', TypeError), (3.22, TypeError)]


@pytest.mark.parametrize('input_int', get_post_by_pk_param)
def test_get_post_by_pk_param(input_int):
    assert len((get_post_by_pk(input_int))) == 1


@pytest.mark.parametrize('input_int, exceptions', get_post_by_pk_exceptions)
def test_get_post_by_pk_exceptions(input_int, exceptions):
    with pytest.raises(exceptions):
        get_post_by_pk(input_int)
