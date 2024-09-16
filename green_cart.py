import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []


driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(products)
assert count > 0

for product in products:
    actual_list.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, 'div/button').click()

print(actual_list)
assert expected_list == actual_list
print('button clicked')

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Code applied ..!']")))
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)

amounts = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
total = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
assert sum == total
#wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='discountAmt']")))
total_amount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

assert  total_amount < total

print('Testing done')
