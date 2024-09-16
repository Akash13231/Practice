import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_obj)
driver.implicitly_wait(10)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

driver.switch_to.frame('iframe-name')
access = driver.find_elements(By.XPATH, "//a[@href='lifetime-access']")
print(len(access))
access[1].click()

driver.switch_to.default_content()     #to switch back from frame to main window

print(driver.title)
