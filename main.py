from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

prefs = {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False
}
motion_w_url = 'https://manager.motionecosystem.com/login'
rsrv_url = 'https://theme3.motionecosystem.com/reservation'

service = Service()
op = Options()
op.add_experimental_option("detach", True)
op.add_experimental_option('excludeSwitches', ['enable-logging'])
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option("useAutomationExtension", False)
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('prefs', prefs)



driver = webdriver.Chrome(options=op, service=service)
driver.get(url=rsrv_url)

user_name_input = driver.find_element(By.XPATH, '//*[@id="reservationName"]')
user_mobile_input = driver.find_element(By.XPATH, '//*[@id="reservationMobile2"]')
user_name_input = driver.find_element(By.XPATH, '//*[@id="sendBtn1"]')



# id_input = driver.find_element(By.XPATH, '//input[@name="mainMemID"]')
# id_input.send_keys("triuptheme3")
# pwd_input = driver.find_element(By.XPATH, '//input[@name="mainMemPwd"]')
# driver.maximize_window()
# pwd_input.send_keys("qwer1234!@#")

# login_btn = driver.find_element(By.CSS_SELECTOR, '.ui.fluid.large.teal.submit.button')
# login_btn.click()

# button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//a[text()="홈페이지 열기"]')))
# button.click()