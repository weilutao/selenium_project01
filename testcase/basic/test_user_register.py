
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from util.util import get_random_str, get_code


class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    def test_register_code_error(self):
        '''
        :return: 注册验证码错误
        '''
        username = 'admin'
        email = '3220859667@qq.com'
        pwd = '123456'
        confirm_pwd = '123456'
        code = '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)

        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirm_pwd)

        self.driver.find_element_by_id('captcha').clear()
        self.driver.find_element_by_id('captcha').send_keys(code)

        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        # alert弹窗弹出后，切换到弹窗
        alert = self.driver.switch_to.alert

        # python断言
        try:
            assert alert.text == expected
        except Exception as e:
            print('test_register_code_error:bug')
        alert.accept()

        sleep(5)

    def test_register_ok(self):
        '''
        :return:注册成功
        '''
        username = get_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirm_pwd = '123456'
        code = ''
        expected = '注册成功，点击确认进行登录。'

        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)

        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirm_pwd)

        code = get_code(self.driver, 'captchaimg')
        self.driver.find_element_by_id('captcha').clear()
        self.driver.find_element_by_id('captcha').send_keys(code)

        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        try:
            assert alert.text == expected
        except Exception as e:
            print('test_register_ok:bug')
        alert.accept()

        sleep(5)
        self.driver.quit()
