import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


op = Options()
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-automation"])

motion_w_url = 'https://manager.motionecosystem.com/login'
driver = webdriver.Chrome(options=op)
driver.get(url=motion_w_url)

# driver.find_element()

class login():
    print("클래스 진입")
    
    
    def success_login():
        print("로그인 시작")
        window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        window_login = driver.find_element(By.NAME,'mainMemID')
        window_login.send_keys('triuptheme3')
        time.sleep(0.5)
        
        window_login = driver.find_element(By.NAME,'mainMemPwd')
        window_login.send_keys('qwer1234!@#')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
    def login_pw_fail():
        window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        window_login = driver.find_element(By.NAME,'mainMemID')
        window_login.send_keys('triuptheme31')
        time.sleep(0.5)
        
        window_login = driver.find_element(By.NAME,'mainMemPwd')
        window_login.send_keys('qwer1234!@#123')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
        err_popup = driver.find_element(By.CLASS_NAME,'ui error message')
        err_popup.click()
        
    def login_null_date():
        # window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        # window_login = driver.find_element(By.NAME,'mainMemID')
        # time.sleep(0.5)
        
        # window_login = driver.find_element(By.NAME,'mainMemPwd')
        # window_login.send_keys('qwer1234!@#123')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        
        err_popup = driver.find_element(By.CLASS_NAME,'ui error message')
        err_popup.click()
        
    def login_null_id():
        
        # window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        # window_login = driver.find_element(By.NAME,'mainMemID')
        # window_login.send_keys('triuptheme31')
        # time.sleep(0.5)
        
        window_login = driver.find_element(By.NAME,'mainMemPwd')
        window_login.send_keys('qwer1234!@#123')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        
        err_popup = driver.find_element(By.CLASS_NAME,'ui error message')
        err_popup.click()
        
    def login_null_pw():
        
        window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        window_login = driver.find_element(By.NAME,'mainMemID')
        window_login.send_keys('triuptheme31')
        time.sleep(0.5)
        
        # window_login = driver.find_element(By.NAME,'mainMemPwd')
        # window_login.send_keys('qwer1234!@#123')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        
        err_popup = driver.find_element(By.CLASS_NAME,'ui error message')
        err_popup.click()

        
        
# login.success_login()
login.login_pw_fail()
# login.login_null_date()
# login.login_null_id()
# login.login_null_pw()
    