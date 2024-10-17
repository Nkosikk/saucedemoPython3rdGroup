from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventorPage:
    title_productText_xpath = "//span[@class='title'][contains(.,'Products')]"

    def __init__(self, driver):
        self.driver = driver

    def verifySuccefulLogin(self):
        wait = WebDriverWait(self.driver, 10)
        productTitleElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.title_productText_xpath)))
        productTitleElement.is_displayed()