import os
from pytesseract import pytesseract
from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
import pyautogui
from PIL import Image
from lib.ShowapiRequest import ShowapiRequest

class testcase1(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        sleep(1)

    def test1(self):
        print('test1')

    def test2(self):
        self.driver.get('http://www.jpress.io/user/register')
        sleep(2)
        agree = self.driver.find_element(By.ID, 'agree').location  # 用rect也可以
        x = agree['x']
        y = agree['y']
        print(agree)
        # print(
        pyautogui.moveTo(x+10, y+130)
        pyautogui.click()
        sleep(5)
        self.driver.quit()

    def test3(self):
        self.driver.get('http://localhost:8080/jpress/user/register')
        sleep(1)
        captchaimg = self.driver.find_element(By.ID, 'captchaimg').rect
        print(captchaimg)
        left = captchaimg['x']
        upper = captchaimg['y']
        right = captchaimg['x'] + captchaimg['width']
        lower = captchaimg['y'] + captchaimg['height']

        file = self.filename()
        self.driver.get_screenshot_as_file(file)
        sleep(1)
        self.driver.quit()
        im = Image.open(file)
        img = im.crop((left, upper, right, lower))
        file2 = self.filename()
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


    def filename(self):
        path = os.path.dirname(os.path.dirname(__file__))
        now = datetime.now()
        time = now.strftime('%Y-%m-%d-%H-%M-%S')
        file_name = path + '\screenshots\\' + time + '.png'
        # print(file_name)
        return file_name

if __name__ == '__main__':
    case = testcase1()
    case.test3()