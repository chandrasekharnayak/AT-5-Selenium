from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver= webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# driver.get_screenshot_as_file('scrn_1.png')

# first_scoll = driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

second_scoll = driver.execute_script('window.scrollBy(0,300)')
driver.get_screenshot_as_file('scrn_300.png')

third_scroll = driver.execute_script('window.scrollBy(300,700)')
driver.get_screenshot_as_file('scrn_700.png')


time.sleep(2)
driver.quit()

iframe/widow
exception