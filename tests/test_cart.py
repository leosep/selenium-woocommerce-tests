from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import BASE_URL

def test_add_to_cart(driver):
    driver.get(BASE_URL)
    assert "Shop" in driver.title

    # Find the first product and click "Add to Cart"
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@class, 'single_add_to_cart_button')]")
    add_to_cart_button.click()
    
    time.sleep(2)

    # Verify that the product has been added to the cart
    cart_button = driver.find_element(By.XPATH, "//a[contains(@class, 'cart-contents')]")
    cart_button.click()

    assert "Your cart is currently empty" not in driver.page_source
