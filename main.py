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


class login():
    def success_login():
        print("로그인 시작")
        login_input = driver.find_element(By.NAME,'mainMemID')
        login_input.clear()
        login_input.send_keys('triuptheme3')
        time.sleep(0.5)
        
        login_input = driver.find_element(By.NAME,'mainMemPwd')
        login_input.clear()
        login_input.send_keys('qwer1234!@#')
        time.sleep(0.5)
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
    def click(class_name,path_name):
        element = driver.find_element(class_name,path_name)
        element.click()
        
        
    def login_pw_fail():
        print("패스워드 오입력")
        login_input = driver.find_element(By.NAME,'mainMemPwd')
        login_input.send_keys('qwer1234!@#123')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(0.5)
        alert_text = driver.switch_to.alert.text
        driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디 또는 비밀번호가 맞지 않습니다. 다시 시도해 주세요.":
            login.login_id_fail()
        else :
            driver.close()
        
    def login_id_fail():
        print("아이디 오입력")
        login_input = driver.find_element(By.NAME,'mainMemID')
        login_input.clear()
        login_input.send_keys('test123')
        time.sleep(0.5)
        
        login_input = driver.find_element(By.NAME,'mainMemPwd')
        login_input.clear()
        login_input.send_keys('qwer1234!@#123')
        time.sleep(0.5)
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(0.5)
        alert_text = driver.switch_to.alert.text
        driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디 또는 비밀번호가 맞지 않습니다. 다시 시도해 주세요.":
            login.success_login()
        else :
            driver.close()
        
    def login_null_date():
        print("아이디/패스워드 미입력")
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        
        alert_text = driver.switch_to.alert.text
        driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디를 입력해 주세요.":
            login.login_null_id()
        else :
            driver.close()
        
    def login_null_id():
<<<<<<< HEAD
        driver.get(url=motion_w_url)
        driver.close()
        # window_login = driver.find_element(By.NAME,'mainMemPwd')
        # window_login.send_keys('qwer1234!@#123')
        
        # login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        # login_btn.click()
        # time.sleep(1)
        
        # alert_text = driver.switch_to.alert.text
        # driver.switch_to.alert.dismiss()
        
        
        
    def login_null_pw():
        driver.get(url=motion_w_url)
        window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        window_login = driver.find_element(By.NAME,'mainMemID')
        window_login.send_keys('triuptheme31')
        time.sleep(0.5)
        
        # window_login = driver.find_element(By.NAME,'mainMemPwd')
        # window_login.send_keys('qwer1234!@#123')
=======
        print("아이디 미입력")
        login_input = driver.find_element(By.NAME,'mainMemPwd')
        login_input.send_keys('qwer1234!@#123')
>>>>>>> 5e9a7d569591e5f4f0da481cbfa42006ad9e7210
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
        time.sleep(1)
        alert_text = driver.switch_to.alert.text
        driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디를 입력해 주세요.":
            login.login_null_pw()
        else :
            driver.close()
        
    def login_null_pw():
        print("패스워드 미입력")
        login_input = driver.find_element(By.NAME,'mainMemID')
        login_input.send_keys('triuptheme31')
        time.sleep(0.5)
        
        login_input = driver.find_element(By.NAME,'mainMemPwd')
        login_input.clear()

        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        alert_text = driver.switch_to.alert.text
        print(alert_text)
        driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "비밀번호를 입력해 주세요.":
            login.login_pw_fail()
        else :
            driver.close()

prefs = {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False
}
motion_w_url = 'https://manager.motionecosystem.com/login'
service = Service()
op = Options()
op.add_experimental_option("detach", True)
op.add_experimental_option('excludeSwitches', ['enable-logging'])
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option("useAutomationExtension", False)
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(service=service, options=op)
driver.get(url=motion_w_url)
driver.maximize_window()

# login.login_null_pw()
login.login_null_date()
# login.login_null_id()
<<<<<<< HEAD
# login.login_null_pw()
=======
# login.login_null_pw()
# login.success_login()

>>>>>>> 5e9a7d569591e5f4f0da481cbfa42006ad9e7210
