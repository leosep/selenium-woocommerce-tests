from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import BASE_URL, USER_CREDENTIALS

def test_login(driver):
    driver.get(f"{BASE_URL}/my-account/")
    
    # Check that the page title is correct
    assert "My Account" in driver.title

    # Find the username and password fields and fill in the data
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(USER_CREDENTIALS["username"])
    password_field.send_keys(USER_CREDENTIALS["password"])

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

    # Verify that the login has been successful
    account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'my-account')]")
    assert account_link.is_displayed(), "The login was not successful."

    # Check if the user is redirected to their account dashboard (depending on your WooCommerce store)
    assert "My Account" in driver.page_source, "The user's account could not be accessed."
