import pytest


@pytest.mark.do
def test1():
    print('test1')


@pytest.mark.undo
def test2():
    print('test2')

