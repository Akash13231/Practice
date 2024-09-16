import time
from selenium import webdriver


# chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_obj)
driver = webdriver.Chrome()
#time.sleep(3)
driver.get('https://selenium-python.readthedocs.io/')
time.sleep(2)
print(driver.title)
print(driver.current_url)
time.sleep(3)