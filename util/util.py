import os
from time import strftime, time, localtime
from lib.ShowapiRequest import ShowapiRequest
from selenium import webdriver
from PIL import Image
import random
import string


def get_code(driver, id):
    '''
    :使用pytesseract和Pillow实现验证码识别
    :param driver:浏览器驱动器
    :param id:验证码元素id
    :return:预期返回验证码字符串
    '''

    t = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
    save_path = os.path.abspath(__file__)[0:-12] + 'screenshots\\'
    picture_name1 = save_path + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    em = driver.find_element_by_id(id)
    # 获取二维码元素的顶点
    left_x = em.location['x']
    left_y = em.location['y']
    right_x = em.size['width'] + left_x
    right_y = em.size['height'] + left_y

    # 获取当前win设备的像素ratio
    dpr = driver.execute_script('return window.devicePixelRatio')
    # print(dpr)

    j_pic = Image.open(picture_name1)
    # 扣取验证码
    y_pic = j_pic.crop((left_x + dpr, left_y + dpr, right_x + dpr, right_y + dpr))

    t = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
    picture_name2 =   save_path + str(t) + '.png'
    # 保存验证码
    y_pic.save(picture_name2)

    # 用第三方接口识别验证码
    r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
    r.addFilePara("image", "{}".format(picture_name2))
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    body = res.json()['showapi_res_body']  # 验证码
    print(res.text)  # 返回验证码信息

    return body


def get_random_str():
    '''
    :return 随机生成字符串
    '''
    code_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return code_str

def get_logger():
    '''
    :return: 获取日志
    '''
    import logging
    import logging.handlers
    import datetime

    # 初始化过程
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('C:/python3.7.0/selenium_project01/logs/all.log',
                                                           when='midnight', backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    f_handler = logging.FileHandler('C:/python3.7.0/selenium_project01/logs/error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    return logger


# 为测试方便使用
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/admin/login')
    get_code(driver, 'captchaImg')
    driver.close()

