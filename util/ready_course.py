from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OA_Course(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://iss.bell.ai/web-login.html')
        self.driver.maximize_window()

    def close_driver(self):
        sleep(5)
        self.driver.close()

    def loading(self):
        '''登录'''
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/input').send_keys('18312840013')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/div/input').send_keys('123456789')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div[2]/button').click()

    def select_class(self):
        # WebDriverWait(self.driver, 5).until(EC.)
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul[1]/li[4]/div').click()
            self.driver.find_element_by_link_text('中心班级列表').click()
        except Exception:
            print('select_class_error')


    def course_scheduling(self):
        '''排课'''
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[5]/button[3]').click()
        self.driver.find_element_by_xpath('//*[@id="foobar"]/div/div/input').click()
        self.driver.find_element_by_class_name('available today current').click()

if __name__ == '__main__':
    ready_course = OA_Course()
    ready_course.loading()
    ready_course.select_class()
    # ready_course.course_scheduling()
    ready_course.close_driver()