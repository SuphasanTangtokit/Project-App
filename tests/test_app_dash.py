# tests/test_app_dash.py
import pytest
from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite
from selenium.webdriver.common.by import By

# --- FIXTURE ---
@pytest.fixture
def dash_duo():
    # Import the Dash app in-process
    app = import_app("src.app_dash")  # module name, no .py
    dash_tester = DashComposite(app)
    dash_tester.start_server()  # start once
    yield dash_tester
    dash_tester.server.stop()  # stop after all tests

# --- NAVIGATION TESTS ---
def test_navigation_to_home(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/")
    dash_duo.wait_for_text_to_equal("#page-content h1, #page-content h2", "Masters BPG Map", timeout=5)

def test_navigation_to_bpgs(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/bpgs")
    dash_duo.wait_for_text_to_equal("#page-content h1, #page-content h2", "THE BPGs", timeout=5)

def test_navigation_to_about(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/about")
    dash_duo.wait_for_text_to_equal("#page-content h2", "ABOUT", timeout=5)

def test_navigation_to_basics(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/basics")
    dash_duo.wait_for_text_to_equal("#page-content h1, #page-content h2", "THE BASICS", timeout=5)

# --- INTERACTION TESTS ---
def test_bpg_detail_page_loads(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/bpgs/Falls%20Prevention")
    dash_duo.wait_for_text_to_equal("#page-content h2", "BPG Detail: Falls Prevention", timeout=5)
    assert "Falls Prevention" in dash_duo.driver.page_source

def test_back_link_from_detail_page(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/bpgs/Falls%20Prevention")
    back_link = dash_duo.driver.find_element(By.LINK_TEXT, "Back to BPG list")
    back_link.click()
    dash_duo.wait_for_text_to_equal("#page-content h1, #page-content h2", "THE BPGs", timeout=5)

# --- ERROR PAGE TEST ---
def test_invalid_page_returns_404(dash_duo):
    dash_duo.driver.get(dash_duo.server_url + "/nonexistentpage")
    dash_duo.wait_for_text_to_equal("#page-content", "404 - Page not found", timeout=5)
    assert "404 - Page not found" in dash_duo.driver.page_source
