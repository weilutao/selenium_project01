from testcase.pom.basePage import BasePage
from selenium.webdriver.common.by import By

class UserLoginPage(BasePage):
    user_input = (By.NAME, 'user')
    pwd_input = (By.NAME, 'pwd')
    login_btn = (By.CLASS_NAME, 'btn')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_login_page(self, user):
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    def input_user(self, user):
        self.clear(*self.user_input)
        self.input_text(user, *self.user_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.input_text(pwd, *self.pwd_input)

    def click_login_btn(self):
        self.click(*self.login_btn)