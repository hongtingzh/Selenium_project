from datetime import datetime
import os
from time import sleep
import random
from PIL import Image
from selenium.webdriver.common.by import By
import string
from lib.ShowapiRequest import ShowapiRequest


def get_code(driver, id):

    captchaimg = driver.find_element(By.ID, id).rect
    print(captchaimg)
    left = captchaimg['x']
    upper = captchaimg['y']
    right = captchaimg['x'] + captchaimg['width']
    lower = captchaimg['y'] + captchaimg['height']

    file = filename()
    driver.get_screenshot_as_file(file)
    sleep(1)
    driver.quit()
    im = Image.open(file)
    img = im.crop((left, upper, right, lower))
    file2 = filename()
    img.save(file2)

    # 获取验证码
    # img2 = Image.open('D:/tool/PyCharm Community Edition 2020.3.5/workspace/Selenium_project/test.png')
    # ttt = pytesseract.image_to_string(img2)
    # print(ttt)

    # python3.6.5
    # 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests

    # r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
    # # r.addFilePara("image", "2021-10-27-11-16-54.png")
    # r.addFilePara("image", file2)
    # r.addBodyPara("typeId", "34")
    # r.addBodyPara("convert_to_jpg", "0")
    # r.addBodyPara("needMorePrecise", "0")
    # res = r.post()
    # print(res.text)  # 返回信息

    r = ShowapiRequest("http://route.showapi.com/2360-1", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
    r.addBodyPara("img_url", file2)
    res = r.post()
    print(res.text)  # 返回信息
    return res.text

def filename():
    path = os.path.dirname(os.path.dirname(__file__))
    now = datetime.now()
    time = now.strftime('%Y-%m-%d-%H-%M-%S')
    file_name = path + '\screenshots\\' + time + '.png'
    # print(file_name)
    return file_name


def gen_random_str():
    em = ''
    num = random.randint(0, 999999)
    zm = string.ascii_letters
    for i in range(6):
        em = em + random.choice(zm)

    s = em + str(num)
    print(s)
    return s


if __name__ == '__main__':
    gen_random_str()