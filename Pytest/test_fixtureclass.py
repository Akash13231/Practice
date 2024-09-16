import pytest


@pytest.mark.usefixtures('setup')
class TestExample:

    def test_fixtureDemo1(self):
        print("fixture demo 1")

    def test_fixturedemo2(self):
        print('fixture demo 2')

    def test_fixturedemo3(self):
        print('fixture demo 3')