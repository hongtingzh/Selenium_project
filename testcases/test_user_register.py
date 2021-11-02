from selenium import webdriver
from time import sleep
from utils.util import gen_random_str
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_User_Register(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/jpress/user/register')

    # 测试注册成功
    def test_register_ok(self):
        pass

    # 账号为空
    def test_register_name_null(self):
        username = ''
        email = '1462367817@qq.com'
        pwd = '123456'
        confirmpwd = '123456'
        captcha = '1234'
        expected = '用户名不能为空'

        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'email').clear()
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'confirmPwd').clear()
        self.driver.find_element(By.NAME, 'confirmPwd').send_keys(confirmpwd)
        self.driver.find_element(By.ID, 'captcha').clear()
        self.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()

        sleep(3)

    def test_register_email_null(self):
        username = gen_random_str()
        email = ''
        pwd = '123456'
        confirmpwd = '123456'
        captcha = '1234'
        expected = '邮箱不能为空'

        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'email').clear()
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'confirmPwd').clear()
        self.driver.find_element(By.NAME, 'confirmPwd').send_keys(confirmpwd)
        self.driver.find_element(By.ID, 'captcha').clear()
        self.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()

        sleep(3)



if __name__ == '__main__':
    case = Test_User_Register()
    case.test_register_name_null()

