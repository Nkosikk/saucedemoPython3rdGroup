from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 10)
        usernameElement = wait.until(EC.visibility_of_element_located((By.ID, self.textbox_username_id)))
        usernameElement.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 10)
        passwordElement = wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id)))
        passwordElement.send_keys(password)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        loginElement = wait.until(EC.visibility_of_element_located((By.ID, self.button_login_id)))
        loginElement.click()


    # ToDo create a code to verify that login is a success = Nhlanhla
