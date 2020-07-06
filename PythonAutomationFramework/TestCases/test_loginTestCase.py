from PageObjects.EndUserPage import EndUserPage
from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass


class TestLoginMethods(BaseClass):

    def test_login(self):

        loginPage = LoginPage(self.driver)
        loginPage.enterLoginDetails()
        loginPage.loginBtnClick()

        endUserPage = EndUserPage(self.driver)
        endUserPage.validateEndUserHomePageDisplayed()
