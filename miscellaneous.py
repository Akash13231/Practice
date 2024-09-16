import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')


chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_obj, options=chrome_options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.implicitly_wait(10)
driver.maximize_window()
driver.execute_script('window.scrollBy(0,1000);')
driver.get_screenshot_as_file('screen.png')
print('done')