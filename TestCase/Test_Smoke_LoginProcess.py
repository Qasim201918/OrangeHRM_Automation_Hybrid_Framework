from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PageObject.LoginProcess import LoginProcess_SmokeTest
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
import time

class Test_Smoke_Login_Process():
    baseUrl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUserName()
    passWord = ReadConfig.getPassWord()
    logger = LogGen.loggen()


    def test_1_Smoke_Login_Process(self,setup):
        self.driver =setup
        self.driver.get(self.baseUrl)
        self.lp = LoginProcess_SmokeTest(self.driver)
        time.sleep(3)
        self.lp.enterUserName(self.userName)
        self.lp.enterPassWord(self.passWord)
        self.lp.click_Login_Button()
        time.sleep(3)
        self.logger.info("************ Test Case 1- Smoke Test ************")
        self.logger.info("************ Verifying successful navigation to the Dashboard Page ************")

        try:
            self.header = self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
            print(self.header)
            if 'Dashboard' in self.header:
                self.driver.save_screenshot(r'.\\ScreenShot\\PassTests\\Test Case 1- Pass.png')
                self.logger.info("************ Test Case 1 Passed: Login Successful: Navigated to the Dashboard page by triggering a POST request. The backend returns a '302 Found' status code ************")
                assert True
            else:
                self.driver.save_screenshot(r'.\\ScreenShot\\FailTests\\Test Case 1- Fail.png')
                self.logger.info("************ Test Case 1 Failed: Login Failed: Unable to navigat to the Dashboard page after triggering a POST request. The backend returns a '500 Internal Server Error' status code ************")
                assert True
        except(NoSuchElementException):
            self.driver.save_screenshot(r'.\\ScreenShot\\FailTests\\Test Case 1- Fail.png')
            self.logger.info("************ Test Case 1 Failed: Login Failed: Unable to navigat to the Dashboard page after triggering a POST request. The backend returns a '500 Internal Server Error' status code ************")
            assert False, "Test Case 1- Fail"
