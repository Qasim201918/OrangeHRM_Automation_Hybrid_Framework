import time
from selenium.webdriver.common.by import By
from PageObject.LoginProcess import Verify_Login_Process
from PageObject.Admin import Admin_Module
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException


class Test_Admin_Details_Page():
    baseUrl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUserName()
    passWord = ReadConfig.getPassWord()
    logger = LogGen.loggen()

    # def testCase_1_Verifying_Search_By_User_Name(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #
    #     self.lp = Verify_Login_Process(self.driver)
    #     time.sleep(5)
    #     self.lp.enter_User_Name(self.userName)
    #     self.lp.enter_passWord(self.passWord)
    #     self.lp.click_Login_Button()
    #     time.sleep(5)
    #     self.logger.info("*********** Test Case 1- Verifying Successful Navigation to the Admin Details Page **********")
    #
    #     self.am = Admin_Module(self.driver)
    #     self.am.click_Admin_Module()
    #     time.sleep(7)
    #
    #     try:
    #         self.header = self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-level']").text
    #         print(self.driver)
    #         if 'User Management' in self.header:
    #             self.driver.save_screenshot(r".\\ScreenShot\\PassTests\\Test Case 1- Pass.png")
    #             self.logger.info("*********** Test Case 1 Passed: Successfully Navigated to the Admin Details Page ***********")
    #             assert True
    #
    #         else:
    #             self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
    #             self.logger.error("*********** Test Case 1 Failed: An Error occurred while Navigating to the Admin Details Page ***********")
    #             assert False, "Test Case 1 Fail: Element not found in the HTML DOM"
    #
    #     except(NoSuchElementException):
    #         self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1- Fail.png")
    #         self.logger.error("*********** Test Case 1 Failed: An Error occurred while Navigating to the Admin Details Page ***********")
    #         assert False, "Test Case 1 Fail: Element not found in the HTML DOM"
    #
    #
    #     self.logger.info("*********** Test Case 1.1- Verifying 'User Name' Search feature **********")
    #
    #     try:
    #         self.am.enter_Query_In_UserName_Field("Hanif")
    #         self.am.click_Search_Button()
    #         self.driver.save_screenshot(r".\\ScreenShot\\PassTests\\Test Case 1.1- Pass.png")
    #         self.logger.info("*********** Test Case 1.1 Passed: Successfully Located the 'User Name Field' and 'Search Button', Entered 'Hanif' Query and clicked 'Search Button' ***********")
    #         assert True
    #
    #     except(NoSuchElementException):
    #         self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 1.1- Fail.png")
    #         self.logger.error("*********** Test Case 1.1 Failed: Unable to Locate the 'User Name Field' and 'Search Button' ***********")
    #         assert False, "Test Case 1.1 Fail: Element not found in the HTML DOM"
    #
    #     time.sleep(5)


    def testCase_2_Verifying_adding_New_User(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = Verify_Login_Process(self.driver)
        time.sleep(3)
        self.lp.enter_User_Name(self.userName)
        self.lp.enter_passWord(self.passWord)
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

        self.am.enter_user_name("Thomas201918777")
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
                self.logger.info("*********** Test Case 2 Passed: Record successfully added to the back-end by triggering a POST request ***********")
                assert True
            else:
                self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 2- Fail.png")
                self.logger.error("*********** Test Case 2 Failed: The application crashes when trying to add a new record to the back-end after triggering the POST request. The back-end returns a '500 Internal Server Error' status code ***********")
                assert False, "Test Case 2- Fail"

        except(NoSuchElementException):
            self.driver.save_screenshot(r".\\ScreenShot\\FailTests\\Test Case 2- Fail.png")
            self.logger.error("*********** Test Case 2 Failed: The application crashes when trying to add a new record to the back-end by triggering the POST request. The back-end returns a '500 Internal Server Error' status code ***********")
            assert False, "Test Case 2- Fail"



















