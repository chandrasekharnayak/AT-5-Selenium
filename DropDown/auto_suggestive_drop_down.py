from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_object=Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')

driver=webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

input_box = driver.find_element(By.ID,'autosuggest').send_keys('ind')

time.sleep(2)
countries = driver.find_elements(By.XPATH,"//li[@role='presentation']/a")
for country in countries:
    print(country)


time.sleep(3)
driver.quit()
