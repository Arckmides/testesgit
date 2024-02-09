from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login import LocatorsLogin

class LoginWebphone(LocatorsLogin):
    #Localizar elementos para realizar login
    def __init__(self, driver):
        self.driver = driver
    
    def insert_email(self, login):
        self.input_insert_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsLogin.input_login))
        self.input_insert_email.send_keys(login)

    def insert_password(self, password):
        self.input_insert_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsLogin.input_password))
        self.input_insert_password.send_keys(password)

    def click_button(self):
        self.click_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsLogin.button))
        self.click_button.click()
