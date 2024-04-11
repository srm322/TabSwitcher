from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import socket

def main():
    
    # Create options variable
    options = Options()

    # set browser settings
    options.add_argument("--kiosk")  # Start Chrome in kiosk mode
    options.add_argument("--disable-notifications")  # Disable notifications
    options.add_argument("--disable-infobars")  # Disable information bars

    # set app location
    options.binary_location = "../chrome/chrome-linux64/chrome"
    # ChromeDriver path var
    chrome_driver_path = "../chrome/chromedriver-linux64/chromedriver"
    # Initialize Chrome
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    
    # Open the window
    driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")
    print("got the driver")
    input("Pausing here [Enter]")
    
    driver.close()
    # hopefully gettin that new new
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")
    input("should wrap up soon...")
    
main()