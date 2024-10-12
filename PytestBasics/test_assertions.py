import pytest

@pytest.mark.smoke
@pytest.mark.xfail
def test_firstprogram1():
    msg = 'Hello'
    assert msg == 'hi', 'test failed'

@pytest.mark.skip
def test_firstprogram2():
    msg = 'Hello'
    assert msg == 'Hello', 'test failed'