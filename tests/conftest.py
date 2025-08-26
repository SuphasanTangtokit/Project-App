# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite

@pytest.fixture(scope="session")
def dash_duo():
    # Edge driver setup
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)

    # Import Dash app
    app = import_app("src.app_dash")  # replace with your path if different

    # DashComposite automatically starts the server
    dash_tester = DashComposite(app, driver=driver)
    dash_tester.start_server()  # important: start local server
    yield dash_tester

    dash_tester.stop_server()  # stop server after tests
    driver.quit()
