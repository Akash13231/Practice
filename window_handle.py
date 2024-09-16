import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID, 'openwindow').click()
window_Handle = driver.window_handles

driver.switch_to.window(window_Handle[1])
print(driver.title)
driver.close()
driver.switch_to.window(window_Handle[0])

print('done')