"""
Sample Selenium Tests for Jenkins CI/CD Learning
=================================================
These tests use headless Chrome to verify basic web interactions.
They are designed to run on Jenkins without a display.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Create a headless Chrome browser instance for each test."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")          # Run without GUI
    chrome_options.add_argument("--no-sandbox")        # Required for Jenkins
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes
    chrome_options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.implicitly_wait(10)

    yield browser          # Give the browser to the test

    browser.quit()         # Close browser after each test


# ── Test 1: Check page title ──────────────────────────────────────────

def test_selenium_homepage_title(driver):
    """Verify the Selenium official site has the correct title."""
    driver.get("https://www.selenium.dev/")
    assert "Selenium" in driver.title, f"Expected 'Selenium' in title, got: {driver.title}"


# ── Test 2: Check an element is visible ───────────────────────────────

def test_selenium_homepage_has_heading(driver):
    """Verify the homepage contains a main heading."""
    driver.get("https://www.selenium.dev/")
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert heading.is_displayed(), "Main heading should be visible"


# ── Test 3: Navigation link works ────────────────────────────────────

def test_documentation_link(driver):
    """Verify the 'Documentation' link navigates correctly."""
    driver.get("https://www.selenium.dev/")
    doc_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Documentation"))
    )
    doc_link.click()
    WebDriverWait(driver, 10).until(EC.url_contains("documentation"))
    assert "documentation" in driver.current_url.lower(), \
        f"Expected 'documentation' in URL, got: {driver.current_url}"
