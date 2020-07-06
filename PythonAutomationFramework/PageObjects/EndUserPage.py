import inspect
from Utilities.BaseClass import BaseClass


class EndUserPage(BaseClass):

    completedJourneys = "h3"

    #   Constructor to use driver
    def __init__(self, driver):
        self.driver = driver

    #   Validate that the User has landed to End User Home Page
    def validateEndUserHomePageDisplayed(self):
        self.verifyWaitUntilForTagName(self.completedJourneys)
        self.grabScreenShot("EndUserHomePage")
        self.reportLogs(inspect.stack()[1][3], "Validated the Credentials", inspect.stack()[1][3], "EndUserHomePage")
        return
