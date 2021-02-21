import pytest


@pytest.fixture()
def init():
    print('init........')
    return 1


def test1(init):
    print('test1')

def test2(init):
    print('test2')

if __name__ == '__main__':
    pytest.main(['-vs', 'test_05.py'])