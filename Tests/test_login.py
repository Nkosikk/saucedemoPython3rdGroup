import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.loginPage import LoginPage
from Utils.readPropeerties_LoginDetails import ReadLoginConfig


class Test_01_Login:
    sauceDemoURL = ReadLoginConfig().getSauceDemoURL()
    username = ReadLoginConfig().getUserName()
    password = ReadLoginConfig().getPassword()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self,setup):
        self.driver=setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.login=LoginPage(self.driver)
        self.login.enterUsername(self.username)
        self.login.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(),name="Login Page",attachment_type=AttachmentType.PNG)

        # delete your name when done
        # ToDo click login button = Sanele
        # ToDo verify home page = Shepherd
        # ToDo select any item = Consy
        # ToDo validated item added to the cart = Zinhle




        time.sleep(2)





