from selenium.webdriver.common.by import By
import time
from config import BASE_URL

def test_checkout(driver):
    driver.get(BASE_URL)
    
    # Add a product to cart
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@class, 'single_add_to_cart_button')]")
    add_to_cart_button.click()
    time.sleep(2)
    
    # Go to cart and proceed to checkout
    cart_button = driver.find_element(By.XPATH, "//a[contains(@class, 'cart-contents')]")
    cart_button.click()
    checkout_button = driver.find_element(By.XPATH, "//a[contains(@class, 'checkout-button')]")
    checkout_button.click()

    assert "Checkout" in driver.title
