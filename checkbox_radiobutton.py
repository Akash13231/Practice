import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


#Checkbox
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkbox))
for i in checkbox:
    if i.get_attribute('value') == 'option2':
        i.click()
        assert i.is_selected()
        break
print('check box clicked')
time.sleep(2)


#radio button
# radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
# print(len(radio))
# for i in radio:
#     if i.get_attribute('value') == 'radio3':
#         i.click()
#         assert i.is_selected()
#         break

radio = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
radio[2].click()
assert radio[2].is_selected()
print('radio is clicked')
time.sleep(2)

assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()

time.sleep(4)
