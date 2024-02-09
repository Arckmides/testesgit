from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from pages.login import LoginWebphone
from pages.login_client import SelectClientWebphone
from time import sleep

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Service)
driver = webdriver.Chrome()

driver.get('https://fone.55pbx.com')
driver.maximize_window()
driver.implicitly_wait(10)

login = LoginWebphone(driver)
login.insert_email('deivid.rocha@55pbx.com.br')
login.insert_password('mzaum8956')
login.click_button()

select_client = SelectClientWebphone(driver)
select_client.insert_client('conta qa')
select_client.select_client()
sleep(10)
