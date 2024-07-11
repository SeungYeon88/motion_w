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

class login:
    
    def success_login():
        window_login = driver.find_element((By.XPATH,'<input type="text" name="mainMemID" placeholder="운영자 아이디" value="" required="">'))
        ActionChains(driver).send_keys_to_element(window_login,"triuptheme3").perform()
        time.sleep(0.5)