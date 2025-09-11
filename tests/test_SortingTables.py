from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    """
    Test Case: Validate that the 'Veg/fruit name' column sorts items alphabetically.

    Steps:
    1. Navigate to the Offers page.
    2. Click the 'Veg/fruit name' column header to trigger sorting.
    3. Collect all veggie names displayed in the table.
    4. Compare browser-sorted list vs. Python's sorted list.

    Args:
        browserInstance (WebDriver): Selenium WebDriver fixture instance
    """
    driver = browserInstance
    browserSortedVeggies = []

    # Open the offers page
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all veggie names -> BrowserSortedveggieList ( A,B, C)
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in veggieWebElements:
        browserSortedVeggies.append(ele.text)

    originalBrowserSortedList = browserSortedVeggies.copy()

    # Sort this BrowserSortedveggieList => newSortedList -> (A,B,C)
    browserSortedVeggies.sort()

    # Assert that browser's sorted list matches Python's sorted list
    assert browserSortedVeggies == originalBrowserSortedList
