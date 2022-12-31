from selenium import webdriver
# Importing by class
from selenium.webdriver.common.by import By
# Importing keys
from selenium.webdriver.common.keys import Keys
import time

class orangehrm():

    def test(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        time.sleep(5)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        time.sleep(5)
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        time.sleep(5)
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        time.sleep(5)
        # Switch to admin tab
        xpath_for_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        switch_to_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Clicking on admin tab
        switch_to_admin.click()
        time.sleep(5)
        # Validating menu options are displaying on Admin page
        element = driver.find_element(By.XPATH, '//nav[@aria-label="Sidepanel"]')
        print(element.is_displayed())
        time.sleep(3)
        # Validating search box is displaying on Admin page
        result_validation = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        print(result_validation.is_displayed())
        time.sleep(3)
        #  Xpath for search button
        xpath_for_search_button = '//input[@placeholder="Search"]'
        search_button = driver.find_element(By.XPATH, xpath_for_search_button)
        # Using for loop to search in upper
        list_1 = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]

        for a in list_1:
            search_button.send_keys(a.upper())
            time.sleep(1)
        # Clearing existing text
            search_button.send_keys(Keys.CONTROL,'a')
            search_button.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        # Using for loop to search in upper
        for a in list_1:
            search_button.send_keys(a.lower())
            time.sleep(1)
        # Clearing existing text
            search_button.send_keys(Keys.CONTROL,'a')
            search_button.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        print("Individual menu are displayed under search box")

abc = orangehrm()
abc.test()
