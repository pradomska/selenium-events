from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=webdriver.ChromeOptions())
url = "https://www.python.org"
driver.get(url)

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

driver.quit()
