import time
from dash.testing.application_runners import import_app
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import requests

def test_line_dropdown(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 2).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )
    navlink.click()  
    selected_item_text = "Aston University"

    # Click on the dropdown to open it
    dropdown = WebDriverWait(dash_duo.driver, 2).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'Select-value-label'))
    )
    dropdown.click()

    # Find the option and click on it
    #options = WebDriverWait(dash_duo.driver, 20).until(
    #    EC.element_to_be_clickable((By.CLASS_NAME, 'VirtualizedSelectOption'))
    #)
    options = WebDriverWait(dash_duo.driver, 2).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'VirtualizedSelectOption')))
    #option_text = option.text
    #option.click()
    option = options[7]
    option_text = option.text
    option.click()

    # Wait for the legend item to appear
    chart_selector = "#line > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.legend > g > g > g:nth-child(2) > text"
    legend_item = WebDriverWait(dash_duo.driver, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, chart_selector))
    )

    # Assertions
    assert option_text == legend_item.text, f"Expected legend item text: {option_text}, Actual: {legend_item.text}"
    #assert selected_item_text in options, f"Dropdown should contain '{selected_item_text}'"
    time.sleep(20) 
    
    
def test_click_pie(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 2).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )
    navlink.click()
    checkbox = dash_duo.driver.find_element(By.ID,"_dbcprivate_radioitems_checklist_input_2020/21")
    checkbox.click()
    css_selector = "#pie > div.js-plotly-plot > div > div > svg:nth-child(1) > g.pielayer > g > g.titletext > text"
    
    chart_title = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    assert ("2020/21" in chart_title.text, "'2021' should appear in the chart title")
    time.sleep(5)
    
def test_slider_interaction(dash_duo):
    # Open the URL of the webpage with the slider
    #driver.get("https://example.com")
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 2).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )
    navlink.click()

    # Locate the slider element
    slider = dash_duo.driver.find_element_by_id("he-provider-slider")

    # Simulate interaction by moving the slider to a specific position
    action = ActionChains(dash_duo.driver)
    action.click_and_hold(slider).move_by_offset(5, 0).release().perform()

    # Wait for the slider to settle and the page to update
    #WebDriverWait(dash_duo.driver, 10).until(EC.text_to_be_present_in_element((By.ID, "result"), "50"))

    # Assert that the slider value has changed as expected
    #result_text = dash_duo.driver.find_element_by_id("result").text
    #assert "50" in result_text, "Slider value is not updated correctly"
def test_server_live(dash_duo):
    """
    GIVEN a dash_duo fixture instance of the server with the app
    WHEN a HTTP request to the home page is made
    THEN the HTTP response status code should be 200
    """

    # Create the app
    app = import_app(app_file="app_dash")
    # Start the server with the app using the dash_duo fixture
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    # You can print this to see what it is e.g. print(f'The server url is {url}')
    url = dash_duo.driver.current_url

    # Make a HTTP request to the server. This uses the Python requests library.
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200
    
def test_home_h1textequals(dash_duo):
    """

    NOTE: dash_duo has a scope of fixture, so you have to start the server each time. There is no stop_server function,
    the dash_duo fixture handles this

    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading text should be "Paralympics Dashboard"
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)

    # Wait for the H1 heading to be visible, timeout if this does not happen within 4 seconds
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the heading has the text we expect
    assert h1_text == "TRANSPORT AND ENVIRONMENT METRICS AT VARIOUS HIGHER EDUCATION PROVIDERS"
def test_nav_link_charts(dash_duo):
    """
    Check the nav link works and leads to the charts page.
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    """dash_duo.wait_for_element("parking", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "parking").click()"""
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Check the page url includes "charts"
    #dash_duo.wait_for_element("parking", timeout=4)
    assert "/spaces" in dash_duo.driver.current_url
"""   
def test_nav_link_energy(dash_duo):
    
    Check the nav link works and leads to the charts page.
    
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("parking", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "parking").click()
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the page url includes "charts"
    #dash_duo.wait_for_element("parking", timeout=4)
    assert "/energy" in dash_duo.driver.current_url
    assert h1_text == "Renewable Energy Page"
"""

def test_barchar_radio(dash_duo):
    
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()
    
    selected_item_text = "2015/16"
    
    dropdown_input = WebDriverWait(dash_duo.driver, 10).until(
        EC.presence_of_element_located((By.ID, "checklist1"))
    )
    
    #dash_duo.wait_for_element_to_be_clickable("dropdown", timeout=2)
     
    dropdown_input.click()
    #dash_duo.wait_for_element("#provider",timeout =30)
    #dash_duo.driver.find_element(By.ID,"provider").click()
    assert selected_item_text in dash_duo.find_element("#checklist1").text, f"Dropdown should contain '{selected_item_text}'"
    time.sleep(5)
    
def test_url(dash_duo):

    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)  # Delay just so I can visually check the page is loaded, this isn't necessary!

    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )
    navlink.click()  

    # Perform actions to navigate to another URL
    # Example: Clicking a link
    link_element = dash_duo.driver.find_element_by_link_text("Go to home page")
    link_element.click()

    # Wait for a brief moment to ensure the page navigation is complete
    time.sleep(2)

    # Get the current URL
    current_url = dash_duo.driver.current_url

    # Assert if the current URL matches the expected URL
    expected_url = "/home"
    assert expected_url in current_url, f"URL mismatch. Expected: {expected_url}, Actual: {current_url}"

def test_radio_barchart(dash_duo):
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    time.sleep(2)
    
    navlink = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.ID, "parking"))
    )

    # Click on the navlink
    navlink.click()  
    
    checkbox = dash_duo.driver.find_element(By.ID,"_dbcprivate_radioitems_checklist1_input_2020/21")
    checkbox.click()
    x_axis_labels_elements=dash_duo.driver.find_elements(By.CLASS_NAME,"xaxislayer-above")
    x_axis_label = "The University of Manchester"
    x_axis_label2 = 'Bath Spa University'#"The University of Reading" 'Bath Spa University'

    x_axis_labels_texts = [label.text for label in x_axis_labels_elements]
    x_axis_labels = [line for label in x_axis_labels_texts for line in label.split('\n')]
    assert x_axis_label not in x_axis_labels, f"Label '{x_axis_label}' not found in x-axis labels"
    assert x_axis_label2 in x_axis_labels #f"Label '{x_axis_label2}' not found in x-axis labels"

    #dash_duo.driver.implicitly_wait(30)
    time.sleep(15)

def test_line_chart_selection(dash_duo):
    
    """GIVEN the app is running
    WHEN the dropdown for the line chart is changed to
    THEN the H1 heading text should be "Paralympics Dashboard"
    """
    
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    dash_duo.driver.implicitly_wait(2)
    css_selector = "#line > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.g-gtitle > text"
    #chart_title = dash_duo.find_element(css_selector)
    chart_title = WebDriverWait(dash_duo.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    assert ("Energy" in chart_title.text, "'Energy' should appear in the chart title")
def test_nav_link_energy(dash_duo):
    """
    Check the nav link works and leads to the charts page.
    """
    app = import_app(app_file="app_dash")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    """dash_duo.wait_for_element("parking", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "parking").click()"""
    
    navlink = WebDriverWait(dash_duo.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "energy"))
    )

    # Click on the navlink
    navlink.click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)
    
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the page url includes "charts"
    #dash_duo.wait_for_element("parking", timeout=4)
    assert "/energy" in dash_duo.driver.current_url
    assert h1_text == "Renewable Energy Page"
    