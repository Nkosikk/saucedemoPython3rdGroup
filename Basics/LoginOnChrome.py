import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome() # This starts the session
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# driver.find_element(By.XPATH,"//span[contains(.,'Products')]").is_displayed()

productText=driver.find_element(By.XPATH,"//span[contains(.,'Products')]").text


if productText=='Products':
    assert True
else:
    assert False


time.sleep(2)
