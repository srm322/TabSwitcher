from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set the path to your ChromeDriver executable
# chrome_driver_path = "./chrome/chromedriver-linux64/chromedriver"
# chrome_driver_path = "./chrome/chrome-linux64/chrome"

# Create options variable
options = Options()

# set browser settings
# options.add_argument("--headless") # Ensure GUI is off
# options.add_argument("--no-sandbox") # These 2 lines used for environment without creen, like for info gathering

# options.add_argument("--kiosk")  # Start Chrome in kiosk mode
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-infobars")  # Disable information bars

# set app location
options.binary_location = "../chrome/chrome-linux64/chrome"
# ChromeDriver path var
chrome_driver_path = "../chrome/chromedriver-linux64/chromedriver"
# Initialize Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
# Initialize Chrome browser
# driver = webdriver.Chrome(executable_path=chrome_driver_path)


# Open the first tab
driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")

# Create New Tab
new_tab_link = "https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=pickleballdisplay#scrollHere"
driver.execute_script(f"window.open('{new_tab_link}', '_blank');")
time.sleep(2)  # Give some time for the new tab to open


# Open window for 25 seconds, then close 
time.sleep(25)
driver.quit()