from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browserutils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):
    """
    Page Object Model class for Checkout Confirmation page.

    Provides methods to perform checkout, enter delivery address,
    and validate successful order placement.
    """

    def __init__(self, driver):
        """
        Initialize with WebDriver instance and define element locators.

        Args:
           driver (WebDriver): Selenium WebDriver instance
        """
        self.driver = driver
        super().__init__(driver)
        self.checkout_button = (By.XPATH, "//button[contains(text(),'Checkout')]")

        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        """
        Click the Checkout button to proceed to order confirmation.
        """
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryName):
        """
        Enter delivery address details and submit the order.

        Args:
          countryName (str): Name of the country to select for delivery
        """

        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        """
        Validate that the order was successfully placed by checking success message.

        Raises:
              AssertionError: If success message does not contain expected text
        """
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText
