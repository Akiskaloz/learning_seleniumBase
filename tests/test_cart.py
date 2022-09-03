from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys

class CartTest(CartPage):
    def setUp(self):
        super().setUp()
        print("Running before test")
        self.open_shop()

    def test_add_to_cart(self):
        # add item to cart
        self.click(self.converse_add)
        # open cart page
        self.click(self.view_cart_btn)
        # or self.open_cart()

        # assert product is added to cart
        self.assert_text('1', self.subtotal_txt)

        # get current subtotal
        text = self.get_text(self.subtotal_txt)
        print(text)
        # change item quantity
        self.set_value(self.quantity_input, '2')
        self.send_keys(self.quantity_input, Keys.RETURN)
        self.click(self.update_cart_btn)

        # Wait for site to load  // site loads too fast loading overlay is never visible
        #self.wait_for_element_visible(self.loading_overlay)
        #self.wait_for_element_not_visible(self.loading_overlay)

        # assert subtotal after item increase
        self.wait_for_text("$300", self.subtotal_txt)   # wait for overload not to be visible, or this should do
        updated_text = self.get_text(self.subtotal_txt)

        self.assertNotEqual(text, updated_text)
