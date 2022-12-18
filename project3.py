from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

#Test case : 3 (PIM)

class username_1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        #Testcase-3

        #xpath for username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

        #xpath for password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(4)

        #xpath for login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

        #xpath for PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

        #xpath for ADD
        ADD_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD=driver.find_element(By.XPATH,ADD_xpath).click()
        time.sleep(4)

        #xpath for FIRSTNAME
        FIRSTNAME_xpath='//input[@placeholder="First Name"]'
        FIRSTNAME=driver.find_element(By.XPATH,FIRSTNAME_xpath).send_keys("vishal")
        time.sleep(4)

        #xpath for LASTNAME
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("jain")
        time.sleep(4)

        #xpath for Save
        Save_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        Save=driver.find_element(By.XPATH,Save_xpath).click()
        time.sleep(7)

        #xpath for Nickname
        Nickname_xpath='//label[text()="Nickname"]/following::div[1]/input'
        Nickname=driver.find_element(By.XPATH,Nickname_xpath).send_keys("chinmy")
        time.sleep(4)

        #xpath for other id
        OtherID_xpath='//label[text()="Other Id"]/following::div[1]/input'
        OtherID=driver.find_element(By.XPATH,OtherID_xpath).send_keys("5687")
        time.sleep(4)

        #xpath for DL
        DL_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        DL=driver.find_element(By.XPATH,DL_xpath).send_keys("158615")
        time.sleep(4)

        #xpath for DL date
        DL_date_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        date=driver.find_element(By.XPATH,DL_date_xpath).send_keys("2025-12-18")
        time.sleep(5)

        #xpath for SSN number
        SSN_xpath='//label[text()="SSN Number"]/following::div[1]/input'
        SSN=driver.find_element(By.XPATH,SSN_xpath).send_keys("1234")
        time.sleep(5)

        #xpath for SIN number
        SIN_xpath = '//label[text()="SIN Number"]/following::div[1]/input'
        SIN = driver.find_element(By.XPATH, SIN_xpath).send_keys("5678")
        time.sleep(5)



        #xpath for DOB
        DOB_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        DOB=driver.find_element(By.XPATH,DOB_xpath).send_keys("1992-05-03")
        time.sleep(5)

        #xpath for Gender
        Gender_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        Gender=driver.find_element(By.XPATH,Gender_xpath).click()
        time.sleep(5)

        #xpath for Militaryservice
        Military_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
        MilitaryService=driver.find_element(By.XPATH,Military_xpath).send_keys("Yes")
        time.sleep(5)

        #xpath for Smoker
        Smoker_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label'
        Smoker=driver.find_element(By.XPATH,Smoker_xpath).click()
        time.sleep(5)

        #xpath to save
        Save_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
        Save=driver.find_element(By.XPATH,Save_xpath).click()
        time.sleep(5)

a=username_1()
a.name_password()