from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("/Users/babak/lighthouse/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Babak")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Shir")
email = driver.find_element(By.NAME, "email")
email.send_keys("babak@gmail.com")
btn = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
# btn.click()

# driver.quit()