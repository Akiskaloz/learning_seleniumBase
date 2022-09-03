from page_objects.shop_page import ShopPage
from selenium.common.exceptions import NoSuchElementException


class ShopTest(ShopPage):
    def test_search_product(self):
        # Open shop page
        self.open_shop()
        # Search product
        self.send_keys(self.search_input, "WhateverHere")
        self.click(self.search_btn)
        # assert product image
        try:
            print("Within Try Block")
            self.assert_element(self.product_img)
        except NoSuchElementException:
            print("Except Block")
            self.assert_text("No products were found matching your selection.", self.no_prod_txt)
