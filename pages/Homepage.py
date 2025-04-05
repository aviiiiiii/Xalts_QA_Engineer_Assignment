import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():

    link_signin =  "//button[text()='Sign In']"
    link_signout = "//button[text()='Sign Out']"

    btn_getStarted = "//button[text()='Get Started']"


    def __init__(self, driver):
        self.driver = driver

    def click_signin_link(self):
        self.driver.find_element(By.XPATH, self.link_signin).click()

    def validate_signup(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.link_signout)))

    def validate_existingUser_alert(self):
        time.sleep(2)
        alert = Alert(self.driver)
        assert alert.text == "Provided E-Mail is already in use"
        alert.accept()

    def click_getStarted_button(self):
        self.driver.find_element(By.XPATH, self.btn_getStarted).click()

    def click_signout_link(self):
        self.driver.find_element(By.XPATH, self.link_signout).click()

    def validate_signout(self):
        return self.driver.find_element(By.XPATH, self.link_signin).is_displayed()
