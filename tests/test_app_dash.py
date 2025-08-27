import pytest
from selenium.webdriver.common.by import By
from dash.testing.wait import until

# --- NAVIGATION TESTS ---
def test_navigation_to_home(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/")
    # Wait until either h1 or h2 contains expected text
    until(lambda: dash_duo.driver.find_element(By.CSS_SELECTOR, "#page-content h1, #page-content h2").text == "Masters BPG Map", timeout=5)
    assert "Masters BPG Map" in dash_duo.driver.page_source

def test_navigation_to_bpgs(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/bpgs")
    until(lambda: dash_duo.driver.find_element(By.CSS_SELECTOR, "#page-content h1, #page-content h2").text == "THE BPGs", timeout=5)
    assert "THE BPGs" in dash_duo.driver.page_source

def test_navigation_to_about(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/about")
    until(lambda: dash_duo.driver.find_element(By.CSS_SELECTOR, "#page-content h2").text == "ABOUT", timeout=5)
    assert "ABOUT" in dash_duo.driver.page_source

def test_navigation_to_basics(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/basics")
    until(lambda: dash_duo.driver.find_element(By.CSS_SELECTOR, "#page-content h1, #page-content h2").text == "THE BASICS", timeout=5)
    assert "THE BASICS" in dash_duo.driver.page_source


# --- INTERACTION TESTS ---
def test_bpg_detail_page_loads(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/bpgs/Falls%20Prevention")
    until(lambda: dash_duo.driver.find_element(By.CSS_SELECTOR, "#page-content h2").text == "BPG Detail: Falls Prevention", timeout=5)
    assert "Falls Prevention" in dash_duo.driver.page_source

def test_back_link_from_detail_page(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/bpgs/Falls%20Prevention")
    back_link = dash_duo.driver.find_element(By.LINK_TEXT, "Back to BPG list")
    back_link.click()
    until(lambda: dash_duo.driver.find_element(By.CSS_SELECTOR, "#page-content h1, #page-content h2").text == "THE BPGs", timeout=5)
    assert "THE BPGs" in dash_duo.driver.page_source


# --- ERROR PAGE TEST ---
def test_invalid_page_returns_404(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/nonexistentpage")
    until(lambda: "404 - Page not found" in dash_duo.driver.page_source, timeout=5)
    assert "404 - Page not found" in dash_duo.driver.page_source
