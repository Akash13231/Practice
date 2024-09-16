from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()


#Static dropdown
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# time.sleep(2)
# dropdown = Select(driver.find_element(By.ID, 'dropdown-class-example'))
# dropdown.select_by_index(2)
# time.sleep(4)



#dynamic dropdoen
chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service= chrome_obj)
driver.get('https://www.google.co.uk/')
time.sleep(3)
driver.find_element(By.ID, "APjFqb").send_keys('ind')
time.sleep(3)
webelement = driver.find_elements(By.TAG_NAME, 'li')
time.sleep(2)
print(len(webelement))

for i in webelement:
    if i.text == 'india map':
        i.click()
        break
assert(driver.find_element(By.ID, "APjFqb").get_attribute('value')) == 'india map'
time.sleep(5)

