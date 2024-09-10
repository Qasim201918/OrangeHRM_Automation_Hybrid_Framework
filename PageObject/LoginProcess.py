from selenium.webdriver.common.by import By

class LoginProcess_SmokeTest():
    UserName_Xpath = "//input[@placeholder='Username']"
    PassWord_Xpath = "//input[@placeholder='Password']"
    Login_Button_Xpath = "//button[@type='submit']"


    def __init__(self,driver):
        self.driver= driver


    def enterUserName(self,username):
        self.driver.find_element(By.XPATH,self.UserName_Xpath).send_keys(username)

    def enterPassWord(self,password):
        self.driver.find_element(By.XPATH,self.PassWord_Xpath).send_keys(password)


    def click_Login_Button(self):
        self.driver.find_element(By.XPATH,self.Login_Button_Xpath).click()
