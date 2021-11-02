from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_Admin_Login(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/jpress/admin/login')

    def test_admin_login_ok(self):
        pass

    def test_admin_login_error(self):
        user = 'adm'
        pwd = '123456'
        captcha = '123'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(user)
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(user)
        self.driver.find_element(By.NAME, 'captcha').clear()
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()

        sleep(3)
