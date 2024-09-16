import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



#chrome_obj = Service("C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
driver.maximize_window()
products = driver.find_elements(By.CLASS_NAME, 'card h-100')


for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == 'Blackberry':
        product.find_element(By.XPATH, 'div/button').click()
        break



driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, 'country').send_keys('ind')

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, 'India').click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

text = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in text
print('done')
