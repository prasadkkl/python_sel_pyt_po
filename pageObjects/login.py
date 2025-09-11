from selenium.webdriver.common.by import By
from pageObjects.Checkout_Confirmation import Checkout_Confirmation
from pageObjects.ShopPage import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    """
    Page Object Model class for the Login Page.
    Provides methods to perform login and navigate to the Shop page.
    """

    def __init__(self, driver):
        """
        Initialize with Selenium WebDriver instance and define element locators.
        Args:
            driver (WebDriver): Selenium WebDriver instance
        """
        self.driver = driver
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):
        """
        Perform login action by entering credentials and clicking the sign-in button.

        Args:
            username (str): Username for login
            password (str): Password for login

        Returns:
            ShopPage: An instance of the ShopPage class after successful login
        """

        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page
