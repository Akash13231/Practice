from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome()
driver.implicitly_wait(5)

expected_list = []
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
opt = driver.find_elements(By.XPATH, '//tr/td[1]')

for i in opt:
    expected_list.append(i.text)

new_list = expected_list.copy()
expected_list.sort()

assert expected_list == new_list
print('done')
