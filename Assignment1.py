import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://rahulshettyacademy.com/loginpagePractise/')

driver.find_element(By.CSS_SELECTOR, '.blinkingText').click()
new_window = driver.window_handles

driver.switch_to.window(new_window[1])
list = (driver.find_element(By.XPATH, "//p[@class='im-para red']").text).split()
#new_list = list.split()
email= list[4]
driver.close()
driver.switch_to.window(new_window[0])

driver.find_element(By.NAME, 'username').send_keys(email)
driver.find_element(By.NAME, 'password').send_keys('learning')

radio = driver.find_elements(By.CSS_SELECTOR, '.customradio')
radio[1].click()
# time.sleep(4)
# alert_msg = driver.switch_to.alert
# alert_msg.accept()
#
# driver.find_element(By.ID, 'terms').click()
# driver.find_element(By.ID, 'signInBtn').click()
# time.sleep(5)

print('all done')
