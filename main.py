import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

op = Options()
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-automation"])

motion_w_url = 'https://manager.motionecosystem.com/login'
driver = webdriver.Chrome(options=op)
driver.get(url=motion_w_url)

# driver.find_element()