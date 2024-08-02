import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


class MenuController:
    def __init__(self):
        return

class ProductCategory:
    def __init__(self, start_url):
        service = Service()
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(url=start_url)
        self.driver.maximize_window()
        self.driver.refresh()

    def product_starter(self):
        self.success_login()
        self.get_list_menu(1)
        self.category_tap(1)
        self.product_null_category_save()
        category_title = self.product_category_save()
        self.view_checkbox_update(category_title)
        # self.category_sort(category_title)
        update_title = self.product_category_update(category_title)
        self.product_category_remove(update_title)

        self.category_tap(2)
        time.sleep(0.5)
        self.product_null_category_save()
        category_title = self.product_category_save()
        self.view_checkbox_update(category_title)
        # self.category_sort(category_title)
        update_title = self.product_category_update(category_title)
        self.product_category_remove(update_title)

    def get_table_list(self, id_value, tag_name):
        category_list = WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located((By.ID, id_value)))
        td_elements = WebDriverWait(category_list[0], timeout=3).until(EC.presence_of_all_elements_located((By.TAG_NAME, tag_name)))
        return td_elements

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        
    def success_login(self):
        window_login = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/input')
        window_login = self.driver.find_element(By.NAME,'mainMemID')
        window_login.send_keys('triuptheme3')
        time.sleep(0.5)
        window_login = self.driver.find_element(By.NAME,'mainMemPwd')
        window_login.send_keys('qwer1234!@#')
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="frmLogin"]/div[1]/button')
        login_btn.click()

    def alert_handler(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            return True
        except NoAlertPresentException:
            return False

    def find_category(self, find_element):
        trise = 0
        while trise <= 3:
            try:
                td_elements = self.get_table_list('dragSort', 'td')
                for element in td_elements:
                    if element.text == find_element:
                        return True
            except StaleElementReferenceException:
                trise += 1
                continue
            break
        return False
    
    def get_menu(self):
        proudct_menu_list = WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="gnbSide"]/div/nav/div[3]/div[1]/div[1]')))
        proudct_menu_list[0].click()
        
    def get_list_menu(self, index):
        self.get_menu()
        proudct_category_menu = WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, f'//*[@id="gnbSide"]/div/nav/div[3]/div[1]/div[2]/div/a[{index}]')))
        proudct_category_menu[0].click()

    def product_null_category_save(self):
        category_save_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div[2]/table/tfoot/tr/th[2]/div/div/button')
        self.scroll_into_view(category_save_btn)
        category_save_btn.click()
        
        alert = self.driver.switch_to.alert
        if alert.text == "카테고리명을 입력해 주세요.":
            alert.dismiss()
            print("alert view check")
        else:
            alert.dismiss()
            print("alert not view")

    def category_tap(self, index):
        proudct_tap = WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, f'/html/body/div[1]/div/div/main/div[1]/div/a[{index}]')))
        proudct_tap[0].click()

    def product_category_save(self):
        save_value = "카테고리 등록 테스트"
        category_save_edit = WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="name"]')))
        category_save_edit[0].send_keys(save_value)
        category_save_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div[2]/table/tfoot/tr/th[2]/div/div/button')
        self.scroll_into_view(category_save_btn)
        time.sleep(1)
        category_save_btn.click()
        
        if self.alert_handler():
            print("카테고리 등록 초과")
            return
        else:
            result = self.find_category(save_value)
            if result:
                print("등록 성공")
            else:
                print("등록 실패")
            time.sleep(1)
        return save_value

    def product_category_remove(self, category_title):
        if category_title:
            save_category = None
            tr_list = self.get_table_list('dragSort', 'tr')
            for tr in tr_list:
                if category_title in tr.text:
                    save_category = tr
            
            if save_category:
                delete_button = WebDriverWait(save_category, 10).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), '삭제')]")))
                delete_button.click()
                WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                self.driver.switch_to.alert.accept()
                result = self.find_category(category_title)
                if result:
                    print("삭제 실패")
                else:
                    print("삭제 성공")
        else:
            print(f"category_title = {category_title}")
            
    def view_checkbox_update(self, category_title):
        tr_list = self.get_table_list('dragSort', 'tr')
        update_tr = None
        for tr in tr_list:
            if category_title in tr.text:
                update_tr = tr
                break
            
        if update_tr:
            view_check_box = WebDriverWait(update_tr, 10).until(EC.presence_of_element_located((By.XPATH, ".//input[@type='checkbox']")))
            check_box_value = view_check_box.is_selected()
            self.driver.execute_script("arguments[0].click();", view_check_box)
            if check_box_value != view_check_box.is_selected():
                print("value change ok")
        else:
            print(f"update_tr: {update_tr}")
                
    def category_sort(self, category_title):
        tr_list = self.get_table_list('dragSort', 'tr')
        update_tr = None
        for tr in tr_list:
            if category_title in tr.text:
                update_tr = tr
                break
        random_tr = random.choice(tr_list)
        print(random_tr.id)
        if update_tr:
            sort_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@class='move text-center ui-sortable-handle']")))
            target = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='{random_tr.id}']")))
            action_chains = ActionChains(self.driver)
            time.sleep(3)
            action_chains.click_and_hold(sort_btn).move_to_element(target).release().perform()
        else:
            print(f"update_tr: {update_tr}")
    
    def product_category_update(self, category_title):
        update_title = "카테고리 수정"
        if category_title:
            save_category = None
            
            time.sleep(1)
            tr_list = self.get_table_list('dragSort', 'tr')
            for tr in tr_list:
                if category_title in tr.text:
                    save_category = tr
                    break
                
            if save_category:
                update_btn = WebDriverWait(save_category, 10).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), '수정')]")))
                update_btn.click()
                update_edit = WebDriverWait(save_category, 10).until(EC.presence_of_element_located((By.XPATH, f".//input[contains(@value, '{category_title}')]")))
                update_edit.clear()
                update_edit.send_keys(update_title)
                update_tr_list = self.get_table_list('dragSort', 'tr')
                update_category = None
                
                for tr in update_tr_list:
                    if "저장" in tr.text:
                        update_category = tr
                        break
                
                update_save_btn = WebDriverWait(update_category, 10).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), '저장')]")))
                update_save_btn.click()
                result = self.find_category(update_title)
                
                if result:
                    print("수정 확인")
                    return update_title
                else:
                    print("수정 실패")
                    
            else:
                print(f"category_title = {category_title}")

class ProductSave():
    def __init__(self):
        return
    def test():
        ProductCategory.get_list_menu(2)
        return

if __name__ == "__main__":
    start_url = "https://manager.motionecosystem.com/"
    # product = ProductCategory(start_url)
    
    # product.product_starter()
    
    