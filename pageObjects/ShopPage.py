from selenium.webdriver.common.by import By
from pageObjects.Checkout_Confirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    """
    Page Object Model class for the Shop Page.

    Provides methods to add products to the cart and navigate to checkout.
    """

    def __init__(self, driver):
        """
        Initialize with Selenium WebDriver instance and define element locators.

        Args:
            driver (WebDriver): Selenium WebDriver instance
        """
        self.driver = driver
        super().__init__(driver)
        self.shop_links = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, product_name):
        """
        Navigate to Shop section and add specified product to the cart.

        Args:
            product_name (str): Name of the product to add to cart
        """
        self.driver.find_element(*self.shop_links).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        """
        Click on the Checkout button and return Checkout_Confirmation page object.

        Returns:
            Checkout_Confirmation: Instance of Checkout_Confirmation class
        """
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        # checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation
