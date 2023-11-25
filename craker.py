import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ervice = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get('https://www.cwa.gov.tw/V8/C/')

try:
    w = driver.find_element(By.CLASS_NAME, 'nav navbar-nav')
    print('有')
except:
    print('失敗')

