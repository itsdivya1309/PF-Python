import pytest

from my_sum import sum


def test_list_int():
    """
    Test that it can sum a list of integers
    """
    data = [1, 2, 3]
    result = sum(data)
    assert result == 6
