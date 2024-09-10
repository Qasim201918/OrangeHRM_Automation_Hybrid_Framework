import time
from selenium.webdriver.common.by import By
from PageObject.LoginProcess import LoginProcess_SmokeTest
from PageObject.Admin import Admin_Module
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException


class Test_Admin_Details_Page():
    baseUrl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUserName()
    passWord = ReadConfig.getPassWord()
    logger = LogGen.loggen()

    def testCase_1_Verifying_Search_By_User_Name(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginProcess_SmokeTest(self.driver)
        time.sleep(3)
        self.lp.enterUserName(self.userName)
        self.lp.enterPassWord(self.passWord)
        self.lp.click_Login_Button()
        time.sleep(5)
        self.logger.info("*********** Test Case 1- Verifying Successful Navigation to the Admin Details Page **********")

        self.am = Admin_Module(self.driver)
        self.am.click_Admin_Module()
        time.sleep(7)

        try:
            self.header = self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-level']").text
            print(self.driver)
            if 'User Management' in self.header:
                self.driver.save_screenshot(r".\\ScreenShot\\PassTests\\Test Case 1- Pass.png")
                self.logger.info("*********** Test Case 1 Passed: Successfully Navigated to the Admin Details Page after triggering a GET request. The backend returns a '200 OK' status code ***********")
                assert True

            else:
                self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
                self.logger.error("*********** Test Case 1 Failed: Unable to Navigate to the Admin Details Page after triggering a GET request. The backend returns a '404 Not Found' status code ***********")
                assert False, "Test Case 1 Fail"

        except(NoSuchElementException):
            self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
            self.logger.error("*********** Test Case 1 Failed: Unable to Navigate to the Admin Details Page after triggering a GET request. The backend returns a '404 Not Found' status code ***********")
            assert False, "Test Case 1 Fail"


        self.logger.info("*********** Test Case 1.1- Verifying 'System Users' Search Bar feature **********")

        try:
            self.am.enter_Query_In_UserName_Field("Admin343434")
            self.am.click_Search_Button()
            time.sleep(10)
            self.header = self.driver.find_element(By.XPATH,"//div[contains(text(),'Admin343434')]").text
            print(self.header)
            if 'Admin343434' in self.header:
             self.driver.save_screenshot(r".\\ScreenShot\\PassTests\\Test Case 1.1- Pass.png")
             self.logger.info("*********** Test Case 1.1 Passed: Successfully Located the 'User Name Field' and 'Search Button', Entered 'Admin343434' Query and clicked 'Search Button' ***********")
             assert True
            else:
                self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1.1- Fail.png")
                self.logger.error("*********** Test Case 1.1 Failed: Unable to Locate the 'User Name Field' and 'Search Button' ***********")
                assert False, "Test Case 1.1 Fail"


        except(NoSuchElementException):
            self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1.1- Fail.png")
            self.logger.error("*********** Test Case 1.1 Failed: Unable to Locate the 'User Name Field' and 'Search Button' ***********")
            assert False, "Test Case 1.1 Fail"
        time.sleep(3)



    def testCase_2_Verifying_adding_New_User(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginProcess_SmokeTest(self.driver)
        time.sleep(3)
        self.lp.enterUserName(self.userName)
        self.lp.enterPassWord(self.passWord)
        self.lp.click_Login_Button()
        time.sleep(3)
        self.logger.info("*********** Test Case 2- Verifying Adding New User **********")

        self.am = Admin_Module(self.driver)
        self.am.click_Admin_Module()
        time.sleep(3)
        self.am.click_Add_New_Button()
        time.sleep(3)

        self.am.click_UserRole_DropDown()

        self.am.select_Admin_User_Role()

        self.am.enter_Employee_Name("Thomas Kutty Benny")
        time.sleep(3)

        # Expand Status dropdown first then click on any option
        self.am.status_DropDown()

        self.am.select_Status()

        self.am.enter_user_name("TesterLab1")
        time.sleep(3)

        self.am.enter_Password("Admin@1238980")

        self.am.enter_Confirm_Password("Admin@1238980")

        self.am.click_Save_Button()
        time.sleep(5)


        try:
            self.header = self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-level']").text
            print(self.header)
            if 'User Management' in self.header:
                self.driver.save_screenshot(r".\\ScreenShot\\PassTests\\Test Case 2- Pass.png")
                self.logger.info("*********** Test Case 2 Passed: Record successfully added to the back-end by triggering a POST request. The back-end returns a '201 Created' status code ***********")
                assert True
            else:
                self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 2- Fail.png")
                self.logger.error("*********** Test Case 2 Failed: The application crashes when trying to add a new record to the back-end after triggering the POST request. The back-end returns a '500 Internal Server Error' status code ***********")
                assert False, "Test Case 2- Fail"

        except(NoSuchElementException):
            self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 2- Fail.png")
            self.logger.error("*********** Test Case 2 Failed: The application crashes when trying to add a new record to the back-end after triggering the POST request. The back-end returns a '500 Internal Server Error' status code ***********")
            assert False, "Test Case 2- Fail"



















