import inspect
import time

import allure
from allure_commons.types import AttachmentType
from Utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    #   Constructor to use driver
    def __init__(self, driver):
        self.driver = driver

    def enterLoginDetails(self):
        self.enterDetailsOnLoginScreen()
        self.reportLogs(inspect.stack()[1][3], "All Details Entered in Login Page", inspect.stack()[1][3],
                        "LoginDetails")
        return

    def loginBtnClick(self):
        time.sleep(2)
        self.grabScreenShot("Login Screen")
        return self.driver.find_element_by_name('commit').click()
