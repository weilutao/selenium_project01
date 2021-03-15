import unittest
from testcase.unittest.test_user_login import TestUserDownload

class Login_yilai(unittest.TestCase):
    def __init__(self, method, login):
        unittest.TestCase.__init__(self, method)
        self.login = login

    def test1(self):
        # 使用的driver都是login里的
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a').click()
        print('test1_ok')

if __name__ == '__main__':
    # 进行测试
    login = TestUserDownload()
    login.test_user_login_success()
    case = Login_yilai(login)
    case.test1()