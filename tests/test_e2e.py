import json

import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import LoginPage
from utils.browserutils import BrowserUtils
from pageObjects.Checkout_Confirmation import Checkout_Confirmation

# test_data_path = '../data/test_e2eTestFramework.json'
test_data_path = r"C:\Users\Prasad\OneDrive\Desktop\Interprep\SeleniumT\PageObject\data\test_e2eTestFramework.json"

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    """
    End-to-End Test Case:
    1. Open Login page
    2. Perform login using test data credentials
    3. Add specified product to cart
    4. Proceed to checkout
    5. Enter delivery address and submit order
    6. Validate success message after order completion

    Args:
        browserInstance (WebDriver): Selenium WebDriver fixture instance
        test_list_item (dict): Test data dict containing userEmail, userPassword, productName
    """
    driver = browserInstance

    # Open login page
    driver.get("http://rahulshettyacademy.com/loginpagePractise/")

    loginPage = LoginPage(driver)
    print(loginPage.getTitle())

    # Perform login and get ShopPage instance
    shop_page = loginPage.login(
        test_list_item["userEmail"], test_list_item["userPassword"]
    )

    # Add product to cart
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())

    # Proceed to checkout
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()

    # Enter delivery address and submit
    checkout_confirmation.enter_delivery_address("ind")

    # Validate order success
    checkout_confirmation.validate_order()
