from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import socket

# Create options variable
options = Options()

# set browser settings
# options.add_argument("--headless") # Ensure GUI is off
# options.add_argument("--no-sandbox") # These 2 lines used for environment without creen, like for info gathering

options.add_argument("--kiosk")  # Start Chrome in kiosk mode
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-infobars")  # Disable information bars

# set app location
options.binary_location = "/usr/bin/chrome/chrome-linux64/chrome"
# ChromeDriver path var
chrome_driver_path = "/usr/bin/chrome/chromedriver-linux64/chromedriver"
# Initialize Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    
# Open the window
driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")

#stahp the darn refresh PLZ
    
try:
    while True:
        try:
            # constant internet testing
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            # reload driver every 2 hours anyways (will most likely delete if working without)
            utc_time = time.gmtime()
            if (utc_time.tm_hour % 2 == 0) and (utc_time.tm_min == 0) and (utc_time.tm_sec <= 5):
                # driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")
                driver.delete_all_cookies()
                driver.refresh()
               
                socket.close()
                
                time.sleep(10) # sleeps beyond if statemen check so that driver only refreshes once.
        
        except socket.error:
            # refresh the browser when connection drops
            driver.refresh()
            # driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")
            time.sleep(15)
                
except KeyboardInterrupt:
    print("\nHello There ;)")
except Exception as e:
    print("\nUnexpected error (or was it): {e}")
finally:    
    print("\n\n It's been an honor.")
    driver.quit()   
    


