import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class page_title():

        def title(self):
            driver = webdriver.Chrome()  # intializes the driver object
            driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
            driver.maximize_window()
            time.sleep(5)

            # adding loggin details with password
            driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
            password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
            password.send_keys('admin123')
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            print("the user loged in successfully")


title = page_title()
title.title()


