import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class page_title():

        def title(self):
            driver = webdriver.Chrome()  # intializes the driver object
            driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
            driver.maximize_window()
            time.sleep(3)

            # adding login details with password
            driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
            password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
            password.send_keys('admin123')
            password.send_keys(Keys.ENTER)
            time.sleep(5)

            #clicking on PIM
            driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]').click()
            time.sleep(5)
            #deleting a employee details
            driver.find_element(By.XPATH,'//button[@class="oxd-icon-button oxd-table-cell-action-space"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()
            time.sleep(5)
            print("successfully deleted")




title = page_title()
title.title()