import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pause
import pyperclip

now = datetime.now()
options = Options()
options.headless = False

driver = webdriver.Chrome(
    executable_path='C:/Users/thsxo/OneDrive/utility/chromedriver.exe',
    options=options)
wait = WebDriverWait(driver, 10)
driver.get(
    'https://devyurim.github.io/python/crawler/2018/08/13/crawler-4.html')

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
