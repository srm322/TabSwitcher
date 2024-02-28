from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create options variable
options = Options()

# set browser settings
# options.add_argument("--headless") # Ensure GUI is off
# options.add_argument("--no-sandbox") # These 2 lines used for environment without creen, like for info gathering

options.add_argument("--kiosk")  # Start Chrome in kiosk mode
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-infobars")  # Disable information bars

# set app location
options.binary_location = "./chrome/chrome-linux64/chrome"
# ChromeDriver path var
chrome_driver_path = "./chrome/chromedriver-linux64/chromedriver"
# Initialize Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

def switch_tabs(driver):
    # Get the handles of all open tabs
    handles = driver.window_handles
    
    # Switch between the tabs
    for handle in handles:
        driver.switch_to.window(handle)
        time.sleep(1)  # Adjust the sleep time if needed

def main():
    # Set the path to your ChromeDriver executable
    chrome_driver_path = "path/to/chromedriver"

    # Initialize Chrome browser
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Open the first tab
    driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")

    # Open a new tab
    driver.execute_script("window.open('','_blank');")

    # Switch to the second tab
    switch_tabs(driver)

    try:
        while True:
            # Perform any actions on the current tab (e.g., navigate, interact with elements)

            # Wait for 3 minutes
            time.sleep(180)

            # Switch to the other tab
            switch_tabs(driver)

    except KeyboardInterrupt:
        # Close the browser when interrupted (Ctrl+C)
        driver.quit()

if __name__ == "__main__":
    main()