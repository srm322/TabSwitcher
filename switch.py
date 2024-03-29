from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import socket

# def background(driver):
#     current_handle = driver.current_window_handle
#     all_handles = driver.window_handles
#     for handle in all_handles:
#         if handle != current_handle:
#             driver.switch_to.window(handle)
#             break

def main():
    
    # Create options variable
    options = Options()

    # set browser settings
    # options.add_argument("--headless") # Ensure GUI is off
    # options.add_argument("--no-sandbox") # These 2 lines used for environment without creen, like for info gathering

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

    # Create New Tab
    # new_tab_link = "https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=pickleballdisplay#scrollHere"
    # driver.execute_script(f"window.open('{new_tab_link}', '_blank');")
    # time.sleep(2)  # Give some time for the new tab to open
    # driver.switch_to.window(driver.window_handles[0])

    # (Test) Switch to the second tab
    # time.sleep(10)
    # driver.switch_to.window(driver.window_handles[1])
    # time.sleep(10)
    # background(driver2)

    try:
        while True:
            try:
                # Wait for ~100 seconds
                # time.sleep(100)
                # driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})
                
                # # Switch to the other tab
                # driver.switch_to.window(driver.window_handles[1])
                
                # Wait for ~100 seconds
                # driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})

                # # Switch to the other tab
                # driver.switch_to.window(driver.window_handles[0])
                
                # Test internet for failure
                time.sleep(3600)
                socket.create_connection(("8.8.8.8", 53), timeout=5)
            
         # Exit on internet outage. systemd will restart (hopefully)
            except socket.error:
                # refresh the browser when connection drops
                # driver.refresh()
                driver.get("https://northstar.greyoakscc.com:8443/northstar/Sports/newTeeSheet.do?activityDisplaySystem=1&stationId=sports#scrollHere")
                time.sleep(10)
    except KeyboardInterrupt:
        print("Hello There ;)")
    except Exception as e:
        print("Unexpected error (or was it): {e}")
    finally:    
        print("\n\n It's been an honor.")
        driver.quit()   
    # while True:{
    #     driver.wait(82800)
    # }
    
    
if __name__ == "__main__":
    main()