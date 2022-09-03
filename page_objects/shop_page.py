from seleniumbase import BaseCase


class ShopPage(BaseCase):
    search_input = "#woocommerce-product-search-field-0"
    search_btn = "button[value='Search']"
    product_img = ".woocommerce-product-gallery__image"
    no_prod_txt = ".woocommerce-info"

    def open_shop(self):
        self.open("https://practice.automationbro.com/shop")
