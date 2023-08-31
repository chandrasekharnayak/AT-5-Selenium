from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service_objcet = Service('C:\ChromeDriver\chromedriver-win32 (1)\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_objcet)

#webdriver :- compoenet --- access the search and it's methodology

driver.get('https://www.hindustantimes.com/')

time.sleep(5)
driver.quit()

#locatoers:-

#id,name,class_name,tagname,link_text,partial_link_text,css_selecetor,xpath

id,name,class,tagname

libk_text and partial_link_text--
css_Selector and Xpath  - static and dynamic work locaters

Xpath :- Absolute Xapth(Static), Relatable Xpath (Dynamic)
