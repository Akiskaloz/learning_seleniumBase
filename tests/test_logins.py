from seleniumbase import BaseCase

class LoginTest(BaseCase):
    def login_user(self):
        self.open("https://practice.automationbro.com/my-account/")
        self.add_text("#username", "testuser")
        self.add_text("#password", "testuser123")
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")



    def setUp(self):
        super().setUp()
        print("Runs before tests")
        self.open("https://practice.automationbro.com/my-account/")
        self.add_text("#username", "testusers1234")
        self.add_text("#password", "testuser!234")
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

    def tearDown(self):

        print("Runs after tests")
        self.open("https://practice.automationbro.com/my-account/")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")

        super().tearDown()  # has to go to the very bottom
