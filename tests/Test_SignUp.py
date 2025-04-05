from pages.Homepage import HomePage
from pages.SigninPage import SigninPage


class Test_SignUp:
    def test_positive_signup(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.enter_email("xalts005@gmail.com")
        print("Email entered")
        signinPage.enter_password("Admin@1234")
        print("Password entered")
        signinPage.enter_confirmPassword("Admin@1234")
        print("Confirm Password entered")
        signinPage.click_submit()
        print("Submit button clicked")
        homePage.validate_signup()
        print("Sign up Successful")

    def test_negative_signup_invalidEmail(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.enter_email("dummy002")
        print("Email entered")
        signinPage.enter_password("Admin@1234")
        print("Password entered")
        signinPage.enter_confirmPassword("Admin@1234")
        print("Confirm Password entered")
        if signinPage.validate_disabled_submit():
            pass
        else:
            raise Exception("Submit button is not disabled")
        print("Submit button is disabled")

    def test_negative_signup_invalidPassword(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.enter_email("dummy002")
        print("Email entered")
        signinPage.enter_password("Admin")
        print("Password entered")
        if signinPage.validate_invalidPassword_error():
            pass
        else:
            raise Exception("Error Message is not displayed")
        print("Error Message is displayed")

    def test_negative_signup_mismatchPassword(self, browserInstance):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.enter_email("dummy002")
        print("Email entered")
        signinPage.enter_password("Admin@1234")
        print("Password entered")
        signinPage.enter_confirmPassword("Admin@12345")
        print("Confirm Password entered")
        if signinPage.validate_mismatchPassword_error():
            pass
        else:
            raise Exception("Error Message is not displayed")
        print("Error Message is displayed")

    def test_negative_signup_sameEmail(self, browserInstance, request):
        driver = browserInstance
        homePage = HomePage(driver)
        homePage.click_signin_link()
        print("Sign-up Clicked")
        signinPage = SigninPage(driver)
        signinPage.enter_email("dummy004@gmail.com")
        print("Email entered")
        signinPage.enter_password("Admin@1234")
        print("Password entered")
        signinPage.enter_confirmPassword("Admin@1234")
        print("Confirm Password entered")
        signinPage.click_submit()
        print("Submit button clicked")
        homePage.validate_existingUser_alert()
        print("Alert Message is displayed")