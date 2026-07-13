from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Path to your chromedriver
service = Service("chromedriver.exe")   # or full path
driver = webdriver.Chrome(service=service)

# Example usage
driver.get("https://www.google.com")
search = driver.find_element("name", "q")
search.send_keys("hello world", Keys.RETURN)
input()