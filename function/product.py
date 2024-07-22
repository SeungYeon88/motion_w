import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, StaleElementReferenceException
import time


class Product():
    def product_starter(driver):
        # Product.success_login(driver)
        Product.product_category_remove(driver)

    def get_table_list(id_value, tag_name):
        category_list = WebDriverWait(driver, timeout=3).until(EC.presence_of_all_elements_located((By.ID, id_value)))
        td_elements = WebDriverWait(category_list[0], timeout=3).until(EC.presence_of_all_elements_located((By.TAG_NAME, tag_name)))
        return td_elements
        
    
    def success_login(driver):
        window_login = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        window_login = driver.find_element(By.NAME,'mainMemID')
        window_login.send_keys('triuptheme3')
        time.sleep(0.5)
        
        window_login = driver.find_element(By.NAME,'mainMemPwd')
        window_login.send_keys('qwer1234!@#')
        
        login_btn = driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()
        
    
    def scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    def alert_handler(driver):
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            return True
        except NoAlertPresentException:
            return False

    def find_category(save_value):
        trise = 0
        while trise <= 3:
            try:
                td_elements = Product.get_table_list('dragSort', 'td')
                
                for element in td_elements:
                        if element.text == save_value:
                            return True
            except StaleElementReferenceException:
                trise += 1
                continue
            break
        return False

    def product_category_save(driver):
        save_value = "카테고리 등록 테스트"
        
        proudct_menu_list = WebDriverWait(driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="gnbSide"]/div/nav/div[3]/div[1]/div[1]')))
        proudct_menu_list[0].click()
        proudct_category_menu = WebDriverWait(driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="gnbSide"]/div/nav/div[3]/div[1]/div[2]/div/a[1]')))
        proudct_category_menu[0].click()
        proudct_tap = WebDriverWait(driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div/a[1]')))
        proudct_tap[0].click()
        category_save_edit = WebDriverWait(driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="name"]')))
        category_save_edit[0].send_keys(save_value)
        category_save_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div[2]/table/tfoot/tr/th[2]/div/div/button')
        Product.scroll_into_view(driver, category_save_btn)
        time.sleep(1)
        category_save_btn.click()
        
        if Product.alert_handler(driver):
            print("카테고리 등록 초과")
        else:
            result = Product.find_category(save_value,driver)
            if result:
                print("등록 성공")
            else:
                print("등록 실패")
            time.sleep(1)

        return save_value

    def product_category_remove(driver):
        category_title = Product.product_category_save(driver)
        if category_title != None:
            tr_list = Product.get_table_list('dragSort', 'tr')

            save_category = None
            
            for tr in tr_list:
                if category_title in tr.text:
                    save_category = tr
            
            if save_category:
                delete_button = WebDriverWait(save_category, 10).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), '삭제')]")))
                delete_button.click()
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                driver.switch_to.alert.accept()
                result = Product.find_category(category_title,driver)
                if result:
                    print("삭제 실패")
                else:
                    print("삭제 성공")
        else:
            print("카테고리 등록실패")
            
            
    def product_category_update(driver):
        category_title = Product.product_category_save(driver)
        if category_title != None:
            save_category = None
            tr_list = Product.get_table_list('dragSort', 'tr')
            
            for tr in tr_list:
                if category_title in tr.text:
                    save_category = tr
            if save_category:
                update_btn = WebDriverWait(save_category, 10).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), '수정')]")))
                update_btn.click()
                update_edit = WebDriverWait(save_category, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='name239']")))
                update_edit.send_keys("카테고리 수정 테스트")
                
            
rsrv_url = 'https://manager.motionecosystem.com/'

service = Service()
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url=rsrv_url)
driver.maximize_window()
driver.refresh()

Product.product_category_update(driver)
