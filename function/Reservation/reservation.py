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



# chrome_options = Options()
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


class reservation():
    
    def success_login():
        
        driver.get(url=motion_w_url)
        
        login_input = driver.find_element(By.NAME,'mainMemID')
        login_input.send_keys('triuptheme3')
        time.sleep(0.5)
        
        login_input = driver.find_element(By.NAME,'mainMemPwd')
        login_input.send_keys('qwer1234!@#')
        time.sleep(0.5)
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
        reservation.reservation()
        
    def reservation():
        rsv_btn = driver.find_element(By.XPATH,'//*[@id="gnbSide"]/div/nav/div[2]/a/i')
        rsv_btn.click()
        
        driver.refresh()
        time.sleep(0.5)
        
        select_filter = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[1]/div[1]/button/i')
        select_filter.click()
        time.sleep(0.5)
        
        # select_period = driver.find_element(By.XPATH,'//*[@id="schForm"]/div/div[1]/div[1]/div[2]/div[2]/button[1]')
        
        # select_period.click()
        select_option = driver.find_element(By.XPATH,'//*[@id="schForm"]/div/div[1]/div[1]/div[2]/div[1]/div/select')
        
        driver.execute_script("arguments[0].click();", select_option)
        
        
        rsrv_option = driver.find_element(By.XPATH,'//*[@id="schForm"]/div/div[1]/div[1]/div[2]/div[1]/div/select/option[2]')
        driver.execute_script("arguments[0].click();", rsrv_option)
        # print(select_period)
        # select_period.click()
        # select_period = driver.find_element(By.CSS_SELECTOR,'#schForm > div > div.ui.form > div:nth-child(1) > div.form-b > div:nth-child(1) > div > select')
        # select_period.click()
        # select.select_by_value("2")
        # select_period.click()
        
        




prefs = {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False
}
motion_w_url = 'https://manager.motionecosystem.com/login'
service = Service()
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


# op = Options()
# op.add_experimental_option("detach", True)
# op.add_experimental_option('excludeSwitches', ['enable-logging'])
# op.add_experimental_option("excludeSwitches", ["enable-automation"])
# op.add_experimental_option("useAutomationExtension", False)
# op.add_argument('--disable-blink-features=AutomationControlled')
# op.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# reservation.success_login()
reservation.reservation()