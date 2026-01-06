from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.product_items = (By.CLASS_NAME, "inventory_item")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def load_webpage(self):
        self.driver.get("https://www.saucedemo.com")

    def login(self):
        self.wait.until(EC.visibility_of_element_located(
            self.username_input)).send_keys("standard_user")
        self.wait.until(EC.visibility_of_element_located(
            self.password_input)).send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def get_all_items(self):
        total_items = self.wait.until(
            EC.presence_of_all_elements_located(self.product_items))
        for item in total_items:
            name = item.find_element(
                By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(
                By.CLASS_NAME, "inventory_item_price").text
            click_button = item.find_element(
                By.XPATH, ".//button[contains(text(),'Add to cart')]")
            click_button.click()
            print(f"✔️{name} is added to cart")

    def badge_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.cart_badge))
        return badge.text
