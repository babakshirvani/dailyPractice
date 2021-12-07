from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("/Users/babak/lighthouse/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=sr_1_3?crid=2IMJIJM1V128D&keywords=instant%2Bpot%2Bduo%2Bevo%2Bplus&qid=1638911897&sprefix=instant%2Bpot%2Bdue%2Bevo%2Bpl%2Caps%2C268&sr=8-3&th=1")
# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text)


driver.get('https://www.python.org')
# search_bar = driver.find_element(By.NAME,"q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CLASS_NAME, "documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


event_times = driver.find_elements(By.CLASS_NAME, "event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CLASS_NAME, "event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()