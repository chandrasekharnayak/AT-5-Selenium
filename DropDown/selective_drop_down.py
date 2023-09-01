from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_object=Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')

driver=webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/client')


register_key=driver.find_element(By.LINK_TEXT,"Register").click()

#this line for first_name data send by end_user
first_name=driver.find_element(By.ID,'firstName').send_keys('Ruchira')

last_name=driver.find_element(By.ID,'lastName').send_keys('Sonawane')

email=driver.find_element(By.ID,'userEmail').send_keys('sonawaneruchi@11gmail.com')

phone_number=driver.find_element(By.ID,'userMobile').send_keys('7387479975')

#Selective DropDown

occupation_selective_drop_down = Select(driver.find_element(By.XPATH,"//select[@formcontrolname='occupation']"))
# occupation_selective_drop_down.select_by_index(2)
# occupation_selective_drop_down.select_by_value('2: Student')
occupation_selective_drop_down.select_by_visible_text('Scientist')


gender=driver.find_element(By.XPATH,"//input[@value='Female']").click()
password=driver.find_element(By.ID,'userPassword').send_keys('Ruchira@11')
confirm_password=driver.find_element(By.ID,'confirmPassword').send_keys('Ruchira@11')
check_box=driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
#register_button=driver.find_element(By.ID,'login').click()
time.sleep(5)
driver.quit()
