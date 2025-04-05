import time

from pages.Homepage import HomePage
from pages.SigninPage import SigninPage


class Test_SignIn:
    def test_positive_signin(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.click_signIn_link()
        print("Sign-In clicked")
        signinPage.enter_email("dummy004@gmail.com")
        print("Email entered")
        signinPage.enter_password("Admin@1234")
        print("Password entered")
        signinPage.click_signIn_button()
        print("Sign In button clicked")
        homePage.validate_signup()
        print("Sign In Successful")

    def test_negative_signin_incorrectEmail(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.click_signIn_link()
        print("Sign-In clicked")
        signinPage.enter_email("dummy@gmail.com")
        print("Email entered")
        signinPage.enter_password("Admin@1234")
        print("Password entered")
        signinPage.click_signIn_button()
        print("Sign In button clicked")
        signinPage.validate_userNotFound_error()
        print("User Not Found Alert Displayed")

    def test_negative_signin_incorrectPassword(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.click_signIn_link()
        print("Sign-In clicked")
        signinPage.enter_email("dummy004@gmail.com")
        print("Email entered")
        signinPage.enter_password("Admin@2121111")
        print("Password entered")
        signinPage.click_signIn_button()
        print("Sign In button clicked")
        signinPage.validate_incorrect_error()
        print("Incorrect E-Mail or Password Alert Displayed")

    def test_forced_login(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_getStarted_button()
        print("Get Started clicked")
        signinPage = SigninPage(driver)
        signinPage.validate_signInPage()
        print("Redirected to Sign In Page")
