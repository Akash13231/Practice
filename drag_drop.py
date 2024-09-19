import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_obj)
driver.implicitly_wait(5)
driver.get('https://demo.automationtesting.in/Static.html')

element1 = driver.find_element(By.XPATH, "//div[@class='col-xs-10 col-xs-offset-2'][1]")
element2 = driver.find_element(By.XPATH, "//div[@class='col-xs-10 col-xs-offset-2'][2]")
element3 = driver.find_element(By.XPATH, "//div[@class='col-xs-10 col-xs-offset-2'][3]")
# print(len(elements))
# #ele = elements[2]
# for element in elements:
#     ele = element.find_element(By.ID, 'node').click()


target = driver.find_element(By.ID, 'droparea')


action = ActionChains(driver)
action.drag_and_drop(element1, target).perform()
action.drag_and_drop(element2, target).perform()
action.drag_and_drop(element3, target).perform()


print('done')

