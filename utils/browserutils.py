class BrowserUtils:
    """
    Utility class providing common browser-related methods for Page Objects.
    """

    def __init__(self, driver):
        """
        Initialize with Selenium WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance
        """
        self.driver = driver

    def getTitle(self):
        """
        Get the title of the current browser page.

        Returns:
            str: Page title
        """
        return self.driver.title
