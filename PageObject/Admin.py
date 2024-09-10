from selenium.webdriver.common.by import By

class Admin_Module():
    Admin_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]/span[1]"
    UserNameField_Xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    SearchButton_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]"


    Add_New_User_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]/i[1]"
    UserRole_Dropdown_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    Admin_User_Role_XPATH = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]"
    Employee_Name_Field_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    Status_DropDown_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]"
    Enable_Status_XPATH = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]"
    Username_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/input[1]"
    PassWord_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]"
    Confirm_Password_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]"
    Save_Button_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]"



    def __init__(self,driver):
        self.driver = driver


    def click_Admin_Module(self):
        self.driver.find_element(By.XPATH,self.Admin_XPATH).click()
    def enter_Query_In_UserName_Field(self,usernamefield):
        self.driver.find_element(By.XPATH,self.UserNameField_Xpath).send_keys(usernamefield)
    def click_Search_Button(self):
        self.driver.find_element(By.XPATH,self.SearchButton_XPATH).click()


    def click_Add_New_Button(self):
        self.driver.find_element(By.XPATH,self.Add_New_User_XPATH).click()
    def click_UserRole_DropDown(self):
        self.driver.find_element(By.XPATH,self.UserRole_Dropdown_XPATH).click()
    def select_Admin_User_Role(self):
        self.driver.find_element(By.XPATH,self.Admin_User_Role_XPATH).click()
    def enter_Employee_Name(self,employee):
        self.driver.find_element(By.XPATH,self.Employee_Name_Field_XPATH).send_keys(employee)
    def status_DropDown(self):
        self.driver.find_element(By.XPATH,self.Status_DropDown_XPATH).click()
    def select_Status(self):
        self.driver.find_element(By.XPATH,self.Enable_Status_XPATH).click()
    def clear_User_name(self):
        self.driver.find_element(By.XPATH,self.Username_XPATH).clear()
    def enter_user_name(self,username):
        self.driver.find_element(By.XPATH,self.Username_XPATH).send_keys(username)
    def enter_Password(self,passwordd):
        self.driver.find_element(By.XPATH,self.PassWord_XPATH).send_keys(passwordd)
    def enter_Confirm_Password(self,confirmpassword):
        self.driver.find_element(By.XPATH,self.Confirm_Password_XPATH).send_keys(confirmpassword)
    def click_Save_Button(self):
        self.driver.find_element(By.XPATH,self.Save_Button_XPATH).click()





