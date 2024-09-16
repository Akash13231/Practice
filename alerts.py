import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(2)
driver.find_element(By.ID, 'alertbtn').click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept() #or we can use alert.dismiss
#alert.dismiss()
print('alert accepted')
