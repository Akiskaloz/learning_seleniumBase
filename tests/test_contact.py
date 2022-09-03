from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        # open page
        self.open("https://practice.automationbro.com/contact")

        # scroll to the form
        self.scroll_to("#evf-submit-277")

        # screenshot with empty fields
        self.save_screenshot("empty_contact_form", "custom_screenshots")

        # fill in all fields
        self.send_keys('.contact-name input', 'Test Name')
        self.send_keys('.contact-email input', 'test@testmail.test')
        self.send_keys('.contact-phone input', '123456789')
        self.send_keys('.contact-message textarea', 'This is a test')

        # take screenshot after filling in
        self.save_screenshot("filled_contact_form", "custom_screenshots")

        # click submit
        self.click("#evf-submit-277")

        # verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")