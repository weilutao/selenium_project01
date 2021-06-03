import pytest
import allure
import os


# 测试之前先登录
@pytest.fixture(scope="session")
def login():
    print('登录成功')


@allure.step("步骤1：点....")
def step_1():
    print('1111')

@allure.step("步骤2：点....")
def step_2():
    print('2222')

@allure.feature("编辑页面")
class TestEditPage():
    '''编辑页面'''

    @allure.story("这是一个xxx的用例")
    def test_3(self, login):
        '''用例描述：先登录，再去执行xxx'''
        step_1()
        step_2()
        print("xxx")

    @allure.story("打开页面a")
    def test_4(self, login):
        '''用例描述：先登录，再执行yyy'''
        print('yyy')


if __name__ == '__main__':
    ''' 生成测试报告必须在命令行执行
        pytest --alluredir ./reports test_07.py
        allure serve ./reports 启动allure 查看报告
    '''
    pytest.main(['-vs', 'test_07.py', '--alluredir=./temp'])
    os.system('allure generate ./temp -o E:/selenium_project01/reports --clean')
    # os.system('allure open E:/selenium_project01/reports')



