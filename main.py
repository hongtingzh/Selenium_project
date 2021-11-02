from testcases.testcase1 import testcase1
from utils import util
from selenium import webdriver
from testcases.test_user_register import Test_User_Register
from testcases.test_user_login import Test_User_Login
from testcases.test_admin_login import Test_Admin_Login

if __name__ == '__main__':
    # testcase1.test1()
    # testcase1.test3()

    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get('http://localhost:8080/jpress/user/register')
    # util.get_code(driver, id='captchaimg')

    # case = Test_User_Register()
    # case.test_register_name_null()
    # case.test_register_email_null()

    # case = Test_User_Login()
    # case.test_user_login_error()
    # case.test_user_login_ok()

    case = Test_Admin_Login()
    case.test_admin_login_error()

