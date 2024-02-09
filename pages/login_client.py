from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_client import LocatorsLoginClient
from selenium.webdriver.common.keys import Keys

class SelectClientWebphone(LocatorsLoginClient):
    #Localizar elementos da tela de seleção de cliente
    def __init__(self, driver):
        self.driver = driver
    
    def insert_client(self, search_client):
        self.input_insert_client = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsLoginClient.input_client))
        self.input_insert_client.send_keys(search_client)
    
    def select_client(self):
        self.span_select_client = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsLoginClient.span_client))
        self.span_select_client.click()
    