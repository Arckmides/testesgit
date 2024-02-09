from selenium.webdriver.common.by import By

class LocatorsLogin(object):
    #Locators para realizar login
    input_login = (By.XPATH, '//*[@id="form-login"]/input[1]')
    input_password = (By.XPATH, '//*[@id="form-login"]/input[2]')
    button = (By.XPATH, '//*[@id="form-login"]/button')
