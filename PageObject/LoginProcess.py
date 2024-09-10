from selenium.webdriver.common.by import By

class Verify_Login_Process():
    UserName_XPATH = "//input[@placeholder='Username']"
    PassWord_XPATH = "//input[@placeholder='Password']"
    loginButton_Xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver



    def enter_User_Name(self,username):
        self.driver.find_element(By.XPATH,self.UserName_XPATH).send_keys(username)


    def enter_passWord(self,password):
        self.driver.find_element(By.XPATH,self.PassWord_XPATH).send_keys(password)



    def click_Login_Button(self):
        self.driver.find_element(By.XPATH,self.loginButton_Xpath).click()
