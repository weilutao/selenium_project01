import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


data = [
    ('', '123456', '账号不能为空'),
    ('admin', '123456', '用户中心'),

]

class TestUserLogin(object):
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:8080/jpress/user/login')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def clear_n(self):
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('pwd').clear()

    @pytest.mark.parametrize('user, pwd, expected', data)
    def test_user_login(self, user, pwd, expected):
        TestUserLogin.clear_n(self)

        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/button').click()

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
    pytest.main(['-sv','test_user_login.py'])
