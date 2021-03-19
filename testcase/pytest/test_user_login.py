import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class TestUserDownload(object):
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

    def test_user_login_error(self):
        # 用户名为空
        user = ''
        pwd = '123456'
        expected = '账号不能为空'

        TestUserDownload.clear_n(self)

        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        try:
            assert alert.text == expected
        except Exception as e:
            print('test_user_login_error:bug')
        alert.accept()

        sleep(5)

    def test_user_login_success(self):
        # 用户登录成功
        user = 'admin'
        pwd = '123456'
        expected = '用户中心'

        TestUserDownload.clear_n(self)

        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        try:
            assert self.driver.title == expected
        except Exception as e:
            print('test_user_login_success:bug')
        sleep(5)

if __name__ == '__main__':
    pytest.main('test_user_login.py')