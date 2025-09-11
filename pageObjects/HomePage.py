from selenium.webdriver.common.by import By


class HomePage:
    """
    Page Object Model class for the Home Page.
    Provides methods to interact with elements on the home page.
    """

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        """
        Initialize with Selenium WebDriver instance.
        Args:
            driver (WebDriver): Selenium WebDriver instance
        """
        self.driver = driver

    def ShopItems(self):
        """
        Locate and return the 'Shop' link WebElement.
        Returns:
          WebElement: The 'Shop' link element
        """
        return self.driver.find_element(*HomePage.shop)
