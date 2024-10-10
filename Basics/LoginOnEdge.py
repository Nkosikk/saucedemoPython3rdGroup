import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

faker=Faker()
firstName=faker.first_name()
lastName=faker.last_name()

username=firstName+lastName+"_"+"7585757"
print(username)

driver=webdriver.Edge() # This starts the session
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
