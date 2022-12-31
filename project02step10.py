from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class username_1():
    def name_password(self):
        driver=webdriver.Edge()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

#xpath to username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(2)

#xpath to password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(2)

#xpath to login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

#xpath for PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

#xpath to emp name search
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Alice")
        time.sleep(4)

#xpath to search button
        driver.find_element(By.XPATH,'//label[text()="Sub Unit"]/following::button[2]').click()
        time.sleep(6)

#xpath to click alice account
        driver.find_element(By.XPATH,'//div[text()="0221"]/following::div[1]').click()
        time.sleep(5)

#xpath to job tab
        driver.find_element(By.XPATH,'//a[text()="Immigration"]/following::div[1]').click()
        time.sleep(4)

#xpath to Terminate button
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(4)

#xpath to termination date
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input').send_keys("2022-12-12")
        time.sleep(4)

#xpath to termination reason
        driver.find_element(By.XPATH,'//label[text()="Termination Reason"]/following::div[3]').click()
        time.sleep(4)

#xpath to termination reason dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Contract Not Renewed"]').click()
        time.sleep(4)

#xpath to Note
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea').send_keys("Nil")
        time.sleep(4)

#xpath to save
        driver.find_element(By.XPATH,'//label[text()="Note"]/following::button[2]').click()
        time.sleep(7)

#xpath to activate
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(7)

#NOTE:Testcase 10 and Testcase 11 are combined together, because if we termainate and again tried to reactivate the terminated user. It's displaying error that no records found. So, I've terminated and activated the same employee with in the same code

a=username_1()
a.name_password()
