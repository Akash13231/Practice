import pytest


def test_firstProgram():
    msg = 'Hello'
    assert msg == 'Hello', 'test failed conditions do not match'

@pytest.mark.smoke
def test_check(setup):
    print('good morning')
