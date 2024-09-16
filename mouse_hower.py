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
action = ActionChains(driver)


action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
time.sleep(4)
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()
time.sleep(4)
print('action done')