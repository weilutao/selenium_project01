# 参数化测试
import pytest

# 列表
data1 = ['123', '456']


@pytest.mark.parametrize('pwd', data1)
def test1(pwd):
    print(pwd)


# 元组
data2 = [
    (1, 2, 3),
    (4, 5, 6)
]


@pytest.mark.parametrize('a, b, c', data2)
def test2(a, b, c):
    print(a, b, c)


# 字典
data3 = (
    {
        'name': 'tom',
        'password': 123456
    },
    {
        'key': '11',
        'value': 112
    }
)


@pytest.mark.parametrize('dic', data3)
def test3(dic):
    print(dic)
