from selenium import webdriver
# Importing by class
from selenium.webdriver.common.by import By
# Importing keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
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
        element = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]')
        time.sleep(3)
        print(element.is_displayed())
        time.sleep(3)
        # Finding xpath for user management tab
        xpath_for_user_mgmt = '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]'
        user_management_tab = driver.find_element(By.XPATH, xpath_for_user_mgmt)
        # Clicking on user management tab
        user_management_tab.click()
        time.sleep(3)
        # Finding xpath for clicking on users
        xpath_for_user = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'
        click_on_user = driver.find_element(By.XPATH, xpath_for_user)
        # Clicking on user management tab
        click_on_user.click()
        time.sleep(3)
        # Finding xpath for clicking on user role tab
        click_on_user_role = '//label[text()="User Role"]/following::div[1]'
        users_dropdown = driver.find_element(By.XPATH, click_on_user_role)
        ActionChains(driver).move_to_element(users_dropdown).click().perform()
        # Validating users role dropdown fields is displaying
        print(users_dropdown.is_displayed())
        time.sleep(5)
        # Finding xpath for clicking on status tab
        click_on_status = "//label[text()='Status']/following::div[1]"
        status_dropdown = driver.find_element(By.XPATH, click_on_status)
        ActionChains(driver).move_to_element(status_dropdown).click().perform()
        # Validating status dropdown fields is displaying
        print(status_dropdown.is_displayed())
        time.sleep(5)
        # # Finding xpath for clicking on user role tab
        # click_on_user_role = '//label[text()="User Role"]/following::div[1]'
        # users_dropdown = driver.find_element(By.XPATH, click_on_user_role)
        # ActionChains(driver).move_to_element(users_dropdown).click().perform()
        # # Validating users role dropdown fields is displaying
        # print(users_dropdown.is_displayed())
        # time.sleep(5)
        # Finding xpath for clicking on admin
        xpath_for_admin = '//div[@role="option"]/span[text()="Admin"]'
        clicking_on_admin = driver.find_element(By.XPATH, xpath_for_admin)
        ActionChains(driver).move_to_element(clicking_on_admin).click().perform()
        # Validating to see below drop down value for Users Role dropdown
        print(clicking_on_admin.is_displayed())
        time.sleep(5)
        # # Finding xpath for clicking on status tab
        # click_on_status_for_enabled = "//label[text()='Status']/following::div[1]"
        # status_dropdown_for_enabled = driver.find_element(By.XPATH, click_on_status_for_enabled)
        # ActionChains(driver).move_to_element(status_dropdown_for_enabled).click().perform()
        # # Validating status dropdown fields is displaying
        # print(status_dropdown_for_enabled.is_displayed())
        # time.sleep(5)
        # Finding xpath for selecting enabled
        xpath_for_enabled = '//div[@role="option"]/span[text()="Enabled"]'
        selecting_enabled = driver.find_element(By.XPATH, xpath_for_enabled)
        ActionChains(driver).move_to_element(selecting_enabled).click().perform()
        # Validating to see below drop down value for Status dropdown
        print(selecting_enabled.is_displayed())
        time.sleep(5)
        # # Finding xpath for clicking on user role tab
        # click_on_user_role_for_ess = '//label[text()="User Role"]/following::div[1]'
        # users_dropdown_for_ess = driver.find_element(By.XPATH, click_on_user_role_for_ess)
        # ActionChains(driver).move_to_element(users_dropdown_for_ess).click().perform()
        # # Validating users role dropdown fields is displaying
        # print(users_dropdown_for_ess.is_displayed())
        # time.sleep(5)
        # Finding xpath for clicking on ESS
        xpath_for_ESS = '//div[@role="option"]/span[text()="ESS"]'
        clicking_on_ess = driver.find_element(By.XPATH, xpath_for_ESS)
        ActionChains(driver).move_to_element(clicking_on_ess).click().perform()
        # Validating to see below drop down value for Users Role dropdown
        print(clicking_on_ess.is_displayed())
        time.sleep(5)
        # # Finding xpath for clicking on status tab
        # click_on_status_for_disabled = "//label[text()='Status']/following::div[1]"
        # status_dropdown_for_disabled = driver.find_element(By.XPATH, click_on_status_for_disabled)
        # ActionChains(driver).move_to_element(status_dropdown_for_disabled).click().perform()
        # # Validating status dropdown fields is displaying
        # print(status_dropdown_for_disabled.is_displayed())
        # time.sleep(5)
        # Finding xpath for selecting disabled
        xpath_for_disabled = '//div[@role="option"]/span[text()="Disabled"]'
        selecting_disabled = driver.find_element(By.XPATH, xpath_for_disabled)
        ActionChains(driver).move_to_element(selecting_disabled).click().perform()
        # Validating to see below drop down value for Status dropdown
        print(selecting_disabled.is_displayed())
        time.sleep(5)

abc = orangehrm()
abc.test()







