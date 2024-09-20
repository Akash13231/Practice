from email.mime import image
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PIL import Image


def test():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach', True)
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # assert "Python" in driver.title
    # driver.find_element(By.ID, "truste-consent-button").click()
    page_title = driver.title
    #print(title)
    test_title = 'Test Login | Practice Test Automation'
    assert 'Test Login' in page_title

    # driver.save_screenshot("image.png")
    # screenshot = Image.open("image.png")
    # screenshot.show()
    driver.find_element(By.ID, 'username').send_keys('student')
    driver.find_element(By.NAME, 'password').send_keys('Password123')
    driver.find_element(By.CLASS_NAME, 'btn').click()
    driver.find_element(By.XPATH, "//a[text()='Home']").click()
    driver.find_element(By.ID, 'menu-item-20').click()
    driver.find_element(By.LINK_TEXT, 'Courses').click()
    driver.find_element(By.ID, 'menu-item-19').click()
    driver.find_element(By.CLASS_NAME, 'menu-item menu-item-type-post_type menu-item-object-page menu-item-18').click()

    driver.save_screenshot("image.png")
    screenshot = Image.open("image.png")
    screenshot.show()
    screenshot.close()
    time.sleep(10)
    driver.quit()


test()