from bs4 import BeautifulSoup as bsoup
import psycopg2 as database_driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import yaml

setup = None

with open("setup.yaml", "r") as stream:
    try:
        setup = yaml.safe_load(stream)
        print(setup)
    except yaml.YAMLError as exc:
        print(exc)
        pass
    pass

connection = database_driver.connect("dbname=%s user=%s password='%s'" % (setup["database"]["name"], setup["database"]["rolename"], setup["database"]["password"]))
cursor = connection.cursor()

# # instantiate a chrome options object so you can set the size and headless preference
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")

# # download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# # current directory
# chrome_driver = os.getcwd() +"/chromedriver"

# # go to Google and click the I'm Feeling Lucky button
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
# driver.get("https://www.google.com")
# # button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dismiss')))
# driver.implicitly_wait(15)
# lucky_button = driver.find_element_by_css_selector("[name=btnI]")
# driver.execute_script("arguments[0].scrollIntoView();", lucky_button)
# driver.implicitly_wait(15)
# # ActionChains(driver).move_to_element(lucky_button).click(lucky_button).perform()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[name=btnI]"))).click()
# # lucky_button.click()

# # capture the screen
# driver.get_screenshot_as_file("capture.png")

cursor.close()
