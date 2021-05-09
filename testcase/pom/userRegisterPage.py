from selenium.webdriver.common.by import By
from testcase.pom.basePage import BasePage
from time import sleep

class UserRegisterPage(BasePage):
    # 首先声明定位器loc
    username_input = (By.NAME, 'username')
    email_input = (By.NAME, 'email')
    pwd_input = (By.NAME, 'pwd')
    confirmPwd_input = (By.NAME, 'confirmPwd')
    captche_input = (By.NAME, 'captche')
    register_btn = (By.CLASS_NAME, 'btn')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_register_page(self):
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_input)
        self.input_text(username, *self.username_input)

    def input_email(self, email):
        self.clear(*self.email_input)
        self.input_text(email, *self.email_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.input_text(pwd, *self.pwd_input)

    def input_confrimPwd(self, confrimPwd):
        self.clear(*self.confirmPwd_input)
        self.input_text(confrimPwd, *self.confirmPwd_input)

    def input_captche(self, captche):
        self.clear(*self.captche_input)
        self.input_text(captche, *self.captche_input)

    def click_register_btn(self):
        self.click(*self.register_btn)
        sleep(2)