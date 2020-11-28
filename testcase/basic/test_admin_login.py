from selenium import webdriver
from util.util import get_code
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestUserDownload(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/jpress/admin/login')

    def test_download_user_error(self):
        user = 'admi'
        pwd = '123456'
        captcha = ''
        expected = '用户名不正确'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('captcha').clear()
        captcha = get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        self.driver.find_element_by_xpath('//*[@id="form"]/div[4]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        try:
            assert alert.text == expected
        except Exception as e:
            print('test_download_user-error:bug')

        alert.accept()

        sleep(5)

    def test_download_pwd_error(self):
        user = 'admin'
        pwd = '12345'
        captcha = ''
        expected = '用户名或密码不正确'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('captcha').clear()
        captcha = get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        self.driver.find_element_by_xpath('//*[@id="form"]/div[4]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        try:
            assert alert.text == expected
        except Exception as e:
            print('test_download_pwd_error:bug')
        alert.accept()

        sleep(5)

        self.driver.quit()
