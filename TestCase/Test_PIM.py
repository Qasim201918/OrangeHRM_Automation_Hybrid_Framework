import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from PageObject.PIM import Pim_Module
from PageObject.LoginProcess import LoginProcess_SmokeTest
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_PIM_Details_Page():
    baseUrl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUserName()
    passWord = ReadConfig.getPassWord()
    logger = LogGen.loggen()


    def test_01_Employee_Information(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginProcess_SmokeTest(self.driver)
        time.sleep(3)
        self.lp.enterUserName(self.userName)
        self.lp.enterPassWord(self.passWord)
        self.lp.click_Login_Button()
        time.sleep(3)
        self.logger.info("*********** Test Case 1- Verifying Employee Information Search functionality ***********")
        self.ei = Pim_Module(self.driver)
        time.sleep(3)
        self.ei.click_PIM_Module()
        time.sleep(3)

        try:
            self.ei.enter_Employee_ID("0295")
            self.ei.click_Search_Button()
            time.sleep(5)
            self. header = self.driver.find_element(By.XPATH,"//div[contains(text(),'0295')]").text
            if '0295' in self.header:
                self.driver.save_screenshot(".\\ScreenShot\\PassTests\\Test Case 1- Pass.png")
                self.logger.info("*********** Test Case 1 Passed: Successfully retrieved data for Employee ID '0295' from the server ***********")
                assert True
            else:
                self.driver.save_screenshot(".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
                self.logger.error("*********** Test Case 1 Failed: The search functionality for 'Employee Information' failed to retrieve data from the backend ***********")
                assert False,"Test Case 1 Failed"
        except(NoSuchElementException):
            self.driver.save_screenshot(".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
            self.logger.error("*********** Test Case 1 Failed: Unable to Locate element on web page by given XPATH ***********")
            assert False,"Test Case 1 Failed"




