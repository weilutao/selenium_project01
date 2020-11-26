from util import util
from selenium import webdriver
from testcase import testcase1
from testcase.basic.test_user_register import TestUserRegister


if __name__ == '__main__':
    # 验证码识别
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get('http://localhost:8080/jpress/user/register')
    # util.get_code(driver, 'captchaimg')

    register = TestUserRegister()
    register.test_register_code_error()
    register.test_register_ok()



