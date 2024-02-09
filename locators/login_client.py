from selenium.webdriver.common.by import By

class LocatorsLoginClient(object):
    #Locators para selecionar cliente
    input_client = (By.ID, 'search-client')
    span_client = (By.XPATH, '//*[@id="select-client"]/button/span[1]/p')
    