import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

url = 'https://manager.motionecosystem.com/login'
driver = webdriver.Chrome(options=options)
driver.get(url=url)

