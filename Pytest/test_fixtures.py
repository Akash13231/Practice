import pytest


@pytest.fixture
def setup():
    print('I will execuate first')

    yield
    print('i will execuate after all test case run beacouse of yield function')


def test_run(setup):
    print('i will execuate after fixtures execuation')