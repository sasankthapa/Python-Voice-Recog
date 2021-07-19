from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

with webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options) as driver:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://www.google.com/")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle
    print(original_window)
    
    #driver.switch_to.new_window('tab')
    wait.until(EC.title_is("Google")) 

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    #wait.until(EC.title_is("SeleniumHQ Browser Automation")) 
    print(driver.title)
    print(driver)
