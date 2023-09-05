from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service_objcet = Service('C:\ChromeDriver\chromedriver-win32 (1)\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_objcet)


driver.get('https://rahulshettyacademy.com/AutomationPractice/')

name = driver.find_element(By.ID,'name').send_keys('Surya DON')
click = driver.find_element(By.ID,'confirmbtn').click()
alret_switch = driver.switch_to.alert
print(alret_switch.text)
# alret_switch.dismiss()
alret_switch.accept()

time.sleep(3)
driver.quit()


#exception, window,scroll,mouse hover