from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service_objcet = Service('C:\ChromeDriver\chromedriver-win32 (1)\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_objcet)

#implicit wait
driver.implicitly_wait(3) # global

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

search_bar = driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
time.sleep(2)
result = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(result)
# assert count>1

for i in result:

    if i.find_element(By.XPATH, 'h4').text == 'Cucumber - 1 Kg':
          continue
    i.find_element(By.XPATH,"div/button").click()

# for i in result:
#
#     if i.find_element(By.XPATH, 'h4').text == 'Raspberry - 1/4 Kg':
#         i.find_element(By.XPATH,"div/button").click()
#     elif i.find_element(By.XPATH, 'h4').text == 'Strawberry - 1/4 Kg':
#         i.find_element(By.XPATH,"div/button").click()


click_add_to_cart_img = driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
click_check_out = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

promo_code = driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys('rahulshettyacademy')
apply = driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()

# code = driver.find_element(By.CSS_SELECTOR,'.promoInfo').text
# print(code)

wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(wait.text)



time.sleep(3)
driver.quit()
