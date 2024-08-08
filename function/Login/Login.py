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


class Login:
    
    def __init__(self, driver):
        self.self.driver = driver
        pass
    
        
    def click(self, class_name,path_name):
        element = self.driver.find_element(class_name,path_name)
        element.click()
        
    def login_pw_fail(self):
        print("패스워드 오입력")
        login_input = self.driver.find_element(By.NAME,'mainMemPwd')
        login_input.send_keys('qwer1234!@#123')
        
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(0.5)
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디 또는 비밀번호가 맞지 않습니다. 다시 시도해 주세요.":
            self.login_id_fail()
        
    def login_id_fail(self):
        print("아이디 오입력")
        login_input = self.driver.find_element(By.NAME,'mainMemID')
        login_input.clear()
        login_input.send_keys('test123')
        time.sleep(0.5)
        
        login_input = self.driver.find_element(By.NAME,'mainMemPwd')
        login_input.clear()
        login_input.send_keys('qwer1234!@#123')
        time.sleep(0.5)
        
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(0.5)
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디 또는 비밀번호가 맞지 않습니다. 다시 시도해 주세요.":
            self.success_login()
        
    def login_null_date(self):
        print("아이디/패스워드 미입력")
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디를 입력해 주세요.":
            self.login_null_id()
        
    def login_null_id(self):
        print("아이디 미입력")
        login_input = self.driver.find_element(By.NAME,'mainMemPwd')
        login_input.send_keys('qwer1234!@#123')
        
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
        time.sleep(1)
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "아이디를 입력해 주세요.":
            self.login_null_pw()
        
    def login_null_pw(self):
        print("패스워드 미입력")
        login_input = self.driver.find_element(By.NAME,'mainMemID')
        login_input.send_keys('triuptheme31')
        time.sleep(0.5)
        
        login_input = self.driver.find_element(By.NAME,'mainMemPwd')
        login_input.clear()

        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        time.sleep(1)
        alert_text = self.driver.switch_to.alert.text
        print(alert_text)
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        if alert_text == "비밀번호를 입력해 주세요.":
            self.login_pw_fail()
            
    def success_login(self):
        print("로그인 시작")
        login_input = self.driver.find_element(By.NAME,'mainMemID')
        login_input.clear()
        login_input.send_keys('triuptheme3')
        time.sleep(0.5)
        
        login_input = self.driver.find_element(By.NAME,'mainMemPwd')
        login_input.clear()
        login_input.send_keys('qwer1234!@#')
        time.sleep(0.5)
        
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        