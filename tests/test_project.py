import pytest


@pytest.mark.xfail
def test_fails():
    assert False, "time to write some tests!"
