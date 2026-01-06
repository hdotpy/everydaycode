from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.landing_page import LandingPage


def test_login(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    landing_page = LandingPage(driver, wait)

    landing_page.load_webpage()
    landing_page.login()

    # Verify successful login by checking the presence of an element on the landing page after login
    assert "inventory.html" in driver.current_url
    landing_page.get_all_items()
    badge_count = landing_page.badge_count()
    assert badge_count == "6", f"Expected 6 items in cart, but got {badge_count}"
