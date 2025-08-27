import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dash.testing.composite import DashComposite
from dash.testing.application_runners import import_app

@pytest.fixture(scope="session")
def dash_duo():
    # Chrome headless setup
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # latest headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Correctly use Service with webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Import Dash app
    app = import_app("src.app_dash")  # path to your Dash app module

    # DashComposite automatically handles server
    dash_tester = DashComposite(app, driver=driver)
    dash_tester.start_server()  # start server once
    yield dash_tester

    dash_tester.stop_server()
    driver.quit()
