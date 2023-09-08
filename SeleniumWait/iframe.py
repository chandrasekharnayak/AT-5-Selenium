from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver= webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.switch_to.frame('courses-iframe')#frame id or frame name
driver.find_element(By.LINK_TEXT,'Mentorship').click()
time.sleep(3)
driver.get_screenshot_as_file('scrn_mentor1.png')

#first you return to your default frame

driver.switch_to.default_content()


time.sleep(2)
driver.quit()


# excepption and multi window