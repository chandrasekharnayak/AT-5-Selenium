from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver= webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/client')

click_forgot_password = driver.find_element(By.LINK_TEXT,'Forgot password?').click()


# time.sleep(2)
# click_login = driver.find_element(By.PARTIAL_LINK_TEXT,'Log').click()

email = driver.find_element(By.XPATH,'//div/form/div[1]/input').send_keys('t@treenetra.in')
password = driver.find_element(By.CSS_SELECTOR,'div form div:nth-child(2) input').send_keys('abc@123')
# conform_password = driver.find_element(By.XPATH,"//input[@formcontrolname='confirmPassword']").send_keys('abc@123')

conform_password_css= driver.find_element(By.CSS_SELECTOR,'#confirmPassword').send_keys('abc@123')
time.sleep(3)
driver.quit()


# Xpath   CSS Selector
# 1.Absolute Xpath --- Static behave  root path  //tag_name/tag_name/tag_name

# 2.Relatable Xpath ---- Dynamic Have

# //tagname[@property='value']
#
# tagname[property='value']


