from selenium.webdriver.common.by import By

class Pim_Module():
    Employee_ID_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]"
    Search_Button_XPATH = "//button[@type='submit']"
    PIM_Modulee_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]"


    def __init__(self,driver):
        self.driver = driver


    def click_PIM_Module(self):
        self.driver.find_element(By.XPATH,self.PIM_Modulee_XPATH).click()
    def enter_Employee_ID(self,id):
        self.driver.find_element(By.XPATH,self.Employee_ID_XPATH).send_keys(id)
    def click_Search_Button(self):
        self.driver.find_element(By.XPATH,self.Search_Button_XPATH).click()



