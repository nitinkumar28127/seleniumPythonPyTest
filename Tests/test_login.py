import time
import pytest
from selenium import webdriver
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage


class TestLogin:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("..\\drivers\\chromedriver.exe")
        driver.implicitly_wait(20)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(10)
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        home=HomePage(driver)
        home.click_welcome()
        home.click_logout()

