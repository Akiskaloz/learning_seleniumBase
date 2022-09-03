from seleniumbase import BaseCase


class CartPage(BaseCase):
    converse_add = "a[aria-label='Add “Branded Converse” to your cart']"
    cart_count_text = "ul[id='primary-menu'] span[class='count']"
    subtotal_txt = "td[class='product-subtotal']"
    quantity_input = "input[id^='quantity']"
    update_cart_btn = "button[name='update_cart']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"
    view_cart_btn = "a[class='added_to_cart wc-forward']"

    def open_cart(self):
        self.open("https://practice.automationbro.com/cart")

    def open_shop(self):
        self.open("https://practice.automationbro.com/shop")
