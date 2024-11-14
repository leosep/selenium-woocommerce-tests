from selenium.webdriver.common.by import By
import time
from config import BASE_URL

def test_filter_by_category(driver):
    driver.get(BASE_URL)

    # Verify that the page loads correctly
    assert "Shop" in driver.title

    # Find and select a category filter
    category_filter = driver.find_element(By.XPATH, "//select[@name='category']")
    category_filter.click()
    category_filter.find_element(By.XPATH, "//option[text()='T-shirts']").click()

    # Wait for the products to update
    time.sleep(2)

    # Verify that the products displayed are from the selected category
    products = driver.find_elements(By.XPATH, "//ul[@class='products']//li")
    for product in products:
        category = product.find_element(By.XPATH, ".//span[contains(@class, 'category')]").text
        assert "T-shirt" in category, f"Product does not belong to the 'T-shirts' category: {category}"

def test_filter_by_price(driver):
    driver.get(BASE_URL)

    # Verify that the page loads correctly
    assert "Shop" in driver.title

    # Find and select a price range filter
    min_price_field = driver.find_element(By.ID, "min_price")
    max_price_field = driver.find_element(By.ID, "max_price")
    apply_filter_button = driver.find_element(By.ID, "filter_submit")

    min_price_field.send_keys("20")
    max_price_field.send_keys("100")
    apply_filter_button.click()

    # Wait for the products to update
    time.sleep(2)

    # Check that the products are within the price range
    products = driver.find_elements(By.XPATH, "//ul[@class='products']//li")
    for product in products:
        price = product.find_element(By.XPATH, ".//span[@class='price']").text
        price_value = float(price.replace('$', '').replace(',', ''))
        assert 20 <= price_value <= 100, f"Product with price out of range: {price_value}"
