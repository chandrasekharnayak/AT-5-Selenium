from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver= webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

def action_chain():
    hover_element = driver.find_element(By.ID,'mousehover')
    actions = ActionChains(driver)
    return actions.move_to_element(hover_element).perform()

action_chain()
top_option = driver.find_element(By.XPATH,"//a[text()='Top']")
time.sleep(2)
top_option.click()


action_chain()
reload = driver.find_element(By.XPATH,"//a[text()='Reload']")
time.sleep(2)
reload.click()




time.sleep(3)
driver.quit()