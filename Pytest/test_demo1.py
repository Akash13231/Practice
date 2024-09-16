#any pytest file should start with or ends with test_ or _test
#pytest method name should start with test_
#any code shoulb be wrapded in a method
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_firstprogram():
    print('hello')


def test_secondprogram():
    print('good morning')
    chrome_obj = Service(
        "C:/Users/abhosage/OneDrive - Capgemini/Desktop/drivers/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_obj)
    driver.implicitly_wait(10)

    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()

    driver.switch_to.frame('iframe-name')
    access = driver.find_elements(By.XPATH, "//a[@href='lifetime-access']")
    print(len(access))
    access[1].click()

    driver.switch_to.default_content()  # to switch back from frame to main window

    print(driver.title)
    driver.quit()