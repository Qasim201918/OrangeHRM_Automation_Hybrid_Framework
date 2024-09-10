import time

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from PageObject.LoginProcess import Verify_Login_Process
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_Login_Process():
    baseUrl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUserName()
    passWord = ReadConfig.getPassWord()
    logger = LogGen.loggen()


    def testCase_Verifying_Login_Process_And_Navigation_To_Dashboard_Page(self,setup):
        self.driver =  setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)

        self.lp = Verify_Login_Process(self.driver)
        self.lp.enter_User_Name(self.userName)
        self.lp.enter_passWord(self.passWord)
        self.lp.click_Login_Button()
        time.sleep(5)
        self.logger.info("************ Test Case 1- Verifying the Login Process by Navigation to the Dashboard Page ************ ")

        try:
         self.header = self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
         print(self.header)
         if 'Dashboard' in self.header:
            self.driver.save_screenshot(r".\\ScreenShot\\PassTests\\Test Case 1- Pass.png")
            self.logger.info("********** Test Case 1 Passed: Successfully Logged in and Navigated to the Dashboard Page **********")
            assert True

         else:
             self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
             self.logger.error("********** Test Case 1 Failed: An error occurred while navigating to Dashboard Page: 'Log in Failed' **********")
             assert False, "Test Case 1 Fail: Element not found in the HTML DOM"

        except(NoSuchElementException):
            self.driver.save_screenshot(r".\\ScreenShot\\NegativeTests\\Test Case 1- Fail.png")
            self.logger.error("********** An error occurred while navigating to Dashboard Page: 'Log in Failed' **********")
            assert False, "Test Case 1 Fail: Element not found in the HTML DOM"

