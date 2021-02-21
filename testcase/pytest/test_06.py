'''
1、 模块级别（setup_module/teardown_module）开始于模块始末，全局
2、 函数级别（setup_function/teardown_function）只对函数用例生效（不在类中）
3、 类级（setup_class/teardown_class）只在类中前后运行一次（在类中）
4、 方法级（setup_method/teardown_method）开始于方法始末（在类中）
5、 类里面的（setup/teardown）运行在调用方法的前后
'''

import pytest

class TestCase(object):
    @classmethod
    def setup_class(self):
        print('setup_class')

    @classmethod
    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test3(self):
        print('test3')

    def test4(self):
        print('test4')

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')

def test1():
    print('test1')

def test2():
    print('test2')

def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')



if __name__ == '__main__':
    pytest.main(['-vs', 'test_06.py'])