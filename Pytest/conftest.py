import pytest


@pytest.fixture(scope='class')
def setup():
    print('I will execuate first')

    yield
    print('i will execute after all test case run beacouse of yield function')


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Akash","Bhosage","AkashBhosage.com"]