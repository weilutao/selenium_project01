
from time import sleep
import pyautogui
from selenium import webdriver


def test1():
    print('case1')


def test2():
    '''
    :点击验证码，使用pyautogui
    '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8080/jpress/user/register')
    elme = driver.find_element_by_id('captchaimg')
    rect = elme.rect
    pyautogui.moveTo(rect['x']+10, rect['y']+130)
    sleep(3)
    pyautogui.click()
    sleep(3)


