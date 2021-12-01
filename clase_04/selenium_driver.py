
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
def get_driver():
    browser_firefox = False 
    if browser_firefox:
        driver_path = '../drivers/geckodriver.exe'
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        driver = Firefox(options=options,executable_path=driver_path)
    else:
        driver_path = '../drivers/chromedriver.exe'
        driver = Chrome(executable_path=driver_path)
    return driver