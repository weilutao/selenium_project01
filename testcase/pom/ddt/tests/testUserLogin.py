import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testcase.pom.ddt.pages.userLoginPage import UserLoginPage


data = [
    ('', '123456', '账号不能为空'),
    ('admin', '123456', '用户中心'),

]

class TestUserLogin(object):
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.loginPage = UserLoginPage(cls.driver)
        cls.loginPage.goto_login_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # def clear_n(self):
    #     self.driver.find_element_by_name('user').clear()
    #     self.driver.find_element_by_name('pwd').clear()

    @pytest.mark.parametrize('user, pwd, expected', data)
    def test_user_login(self, user, pwd, expected):

        self.loginPage.input_user(user)
        self.loginPage.input_pwd(pwd)
        self.loginPage.click_login_btn()

        if user == '':
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert

            # 验证
            assert alert.text == expected
            alert.accept()
        else:
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            #验证
            assert self.driver.title == expected

if __name__ == '__main__':
    pytest.main(['-sv','testUserLogin.py'])
