import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class SigninPage():

    txt_email = "//label[text()='E-Mail']/following-sibling::div/input"
    txt_password = "//label[text()='Password']/following-sibling::div/input"
    txt_confirmPassword = "//label[text()='Confirm Password']/following-sibling::div/input"
    btn_submit = "//button[text()='Sign Up']"

    txt_invalidPassword_error = "//p[text()='Password must contain atelast one lowercase letter, uppercase letter, number and special character and be a minimum of 8 characters in length']"
    txt_mismatchPassword_error = "//p[text()='Passwords do not match']"

    link_signin = "//button[text()='Already have an account? Click here to sign in.']"

    button_signin = "//button[text()='Sign In']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password).send_keys(password)

    def enter_confirmPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_confirmPassword).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.btn_submit).click()

    def validate_disabled_submit(self):
        if self.driver.find_element(By.XPATH, self.btn_submit).is_enabled() :
            return False
        else :
            return True

    def validate_invalidPassword_error(self):
        time.sleep(1)
        return self.driver.find_element(By.XPATH, self.txt_invalidPassword_error).is_displayed()

    def validate_mismatchPassword_error(self):
        time.sleep(1)
        return self.driver.find_element(By.XPATH, self.txt_mismatchPassword_error).is_displayed()

    def click_signIn_link(self):
        self.driver.find_element(By.XPATH, self.link_signin).click()

    def click_signIn_button(self):
        self.driver.find_element(By.XPATH, self.button_signin).click()

    def validate_userNotFound_error(self):
        time.sleep(2)
        alert = Alert(self.driver)
        assert alert.text == "User not found"
        alert.accept()

    def validate_incorrect_error(self):
        time.sleep(2)
        alert = Alert(self.driver)
        assert alert.text == "Incorrect E-Mail or Password"
        alert.accept()

    def validate_signInPage(self):
        time.sleep(1)
        return self.driver.find_element(By.XPATH, self.txt_email).is_displayed()





