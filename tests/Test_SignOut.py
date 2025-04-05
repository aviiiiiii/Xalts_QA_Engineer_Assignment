from pages.Homepage import HomePage
from pages.SigninPage import SigninPage


class Test_SignOut:
    def test_positive_signout(self, browserInstance):
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
        homePage.click_signout_link()
        print("Sign-out Clicked")

        if homePage.validate_signout():
            pass
        else:
            raise Exception("Error while signing out")
        print("Signed out successfully")