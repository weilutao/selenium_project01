from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time



class OA_Course(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('')
        self.driver.maximize_window()

    def close_driver(self):
        sleep(5)
        self.driver.close()

    def loading(self):
        '''登录'''
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/input').send_keys('')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/div/input').send_keys('')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div[2]/button').click()

    def select_class(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/ul[1]/li[4]/div'))).click()
            sleep(1)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '中心班级列表'))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(),'魏禄涛')]"))).click()
        except Exception as e:
            print(e)

    def course_scheduling(self):
        '''排课'''
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[5]/button[3]/span[contains(text(), "单节排课")]'))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="foobar"]/div/div/input'))).click()
        # 选择上课日期
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "今天")]'))).click()
        # 选择上课时间
        H_time = time.strftime("%H", time.localtime())
        M_time1 = time.strftime("%M", time.localtime())
        M_time = str(int(M_time1)//5*5)
        current_time = "{0}:{1}".format(H_time, M_time)
        # print(type(current_time), current_time)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div/input'))).click()
        # 定位下拉框
        # x_path = "//div[contains(text(), '%s')]" % current_time
        # print(type(x_path), x_path)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), '%s')]" %current_time))).click()
        # 选择课时类型
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[1]/div[2]/div/div/div[4]/div[1]/div/div/div/div[2]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "机器人大赛")]'))).click()
        # 选择上课时长
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div/div[1]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '30分钟')]"))).click()
        # 选择课程种类
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[8]/div/div[1]/ul/li[1]'))).click()
        # 选择课程小类
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div/div[1]/input'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[9]/div/div[1]/ul/li[1]'))).click()
        try:
            # 选择课程
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/label/span[2]'))).click()
            # 点击保存
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[3]/button[1]'))).click()
        except Exception as e:
            print("错误的原因：", repr(e))


if __name__ == '__main__':
    ready_course = OA_Course()
    ready_course.loading()
    ready_course.select_class()
    ready_course.course_scheduling()
    ready_course.close_driver()
