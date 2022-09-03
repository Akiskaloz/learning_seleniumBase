from seleniumbase import BaseCase


class HomePage(BaseCase):
    logo_icon = ".custom-logo-link"
    get_started_btn = "#get-started"
    heading_text = "h1"
    site_footer = ".tg-site-footer-section-1"
    menu_links = "li[id*='menu-item-']"
    user_name = "#username"
    password = "#password"
    login_btn = "button[name=login]"
    logout_txt = ".woocommerce-MyAccount-content"
    logout_btn = ".woocommerce-MyAccount-content a[href*=logout]"

    def open_home_page(self):
        # open home page
        self.open("https://practice.automationbro.com")

    def login_user(self):
        self.open("https://practice.automationbro.com/my-account/")
        self.add_text(HomePage.user_name, "testusers1234")
        self.add_text(HomePage.password, "testuser!234")
        self.click(HomePage.login_btn)
        self.assert_text("Log out", HomePage.logout_txt)
        print("Managed to log in")

    def logout_user(self):
        self.open("https://practice.automationbro.com/my-account/")
        self.click(HomePage.logout_btn)
        self.assert_element_visible(HomePage.login_btn)
