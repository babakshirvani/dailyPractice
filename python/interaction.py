from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("/Users/babak/lighthouse/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(article_count.text)

driver.quit()