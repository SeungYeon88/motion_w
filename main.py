import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from function.Login.Login import *




prefs = {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False
}
motion_w_url = 'https://manager.motionecosystem.com/login'
service = Service()
op = Options()
login = Login()

op.add_experimental_option("detach", True)
op.add_experimental_option('excludeSwitches', ['enable-logging'])
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option("useAutomationExtension", False)
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(service=service, options=op)
driver.get(url=motion_w_url)
driver.maximize_window()


login.login_null_date(driver)


