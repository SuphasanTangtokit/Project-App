import pytest
from selenium.webdriver.common.by import By

# All tests here assume that your app is running locally on http://127.0.0.1:8050
# You’ll run these with pytest-dash (dash_duo fixture)

# --- NAVIGATION TESTS ---
def test_navigation_to_home(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/")
    assert "Masters BPG Map" in dash_duo.driver.page_source


def test_navigation_to_bpgs(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/bpgs")
    assert "BPGs" in dash_duo.driver.page_source


def test_navigation_to_about(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/about")
    assert "About" in dash_duo.driver.page_source


def test_navigation_to_thebasics(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/thebasics")
    assert "The Basics" in dash_duo.driver.page_source


# --- INTERACTION TESTS ---
def test_he_provider_slider_updates_chart(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/")
    slider = dash_duo.driver.find_element(By.ID, "he-provider-slider")
    slider.click()
    chart_title = dash_duo.driver.find_element(By.ID, "chart-title")
    assert "2020/21" in chart_title.text, "'2020/21' should appear in the chart title"


def test_subject_dropdown_updates_chart(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/")
    dropdown = dash_duo.driver.find_element(By.ID, "subject-dropdown")
    dropdown.click()
    option = dash_duo.driver.find_element(By.XPATH, "//option[text()='Energy']")
    option.click()
    chart_title = dash_duo.driver.find_element(By.ID, "chart-title")
    assert "Energy" in chart_title.text, "'Energy' should appear in the chart title"


# --- ERROR PAGE TEST ---
def test_invalid_page_returns_404(dash_duo):
    dash_duo.driver.get("http://127.0.0.1:8050/nonexistentpage")
    assert "404" in dash_duo.driver.page_source or "Not Found" in dash_duo.driver.page_source
