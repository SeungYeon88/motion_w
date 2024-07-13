from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
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
driver.maximize_window()
driver.refresh()

user_name_input = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reservationName"]')))
user_mobile_input = driver.find_element(By.XPATH, '//*[@id="reservationMobile2"]')
auth_number_send_btn = driver.find_element(By.XPATH, '//*[@id="sendBtn1"]')
gender_radio = driver.find_elements(By.XPATH, '//*[@name="gender"]')
random_radio = random.choice(gender_radio)

request_input = driver.find_element(By.XPATH, '//*[@id="reservationMemo"]')
# all_agree_checkbox = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="chkAll"]')))
# driver.execute_script("arguments[0].scrollIntoView();", all_agree_checkbox)
# all_agree_checkbox.click()

user_name_input.send_keys("김지헌")
user_mobile_input.send_keys("74417631")
random_radio.click()
request_input.send_keys("요청사항 테스트")

driver.implicitly_wait(2)
date_list = driver.find_elements(By.XPATH, '//*[@id="calendar"]/div/table/tbody/tr[3]/td[2]')
random_date = random.choice(date_list)
random_date.click()

time.sleep(1)
time_list = driver.find_elements(By.XPATH, '//*[@id="serviceTime"]/li[3]/span')
random_tiem = random.choice(time_list)
random_tiem.click()

tiket_append = driver.find_element(By.XPATH, '//*[@id="reservationListDiv"]/div/section[1]/div[1]/button')
tiket_append.click()
# auth_number_send_btn.click()

tiket_items = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="idChk"]')))
random_tiket = random.choices(tiket_items)
print(random_tiket)
for item in random_tiket:
    print(item)
    random_tiket[item].click()