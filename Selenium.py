from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time


chrome_driver = 'C:/Users/User/PycharmProjects/algorithm1/chromedriver'
driver = webdriver.Chrome(chrome_driver)
driver.get('https://www.python.org')
search = driver.find_element_by_id('id-search-field')
search.clear()
time.sleep(2)
search.send_keys('lambda')
time.sleep(3)
search.send_keys(Keys.RETURN)
time.sleep(3)
driver.close()