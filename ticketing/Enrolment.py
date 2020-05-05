import time
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

# 아이디와 패스워드를 여기에 입력
ID = "thsvkd"
PW = "Thsxogud1!"
URL = ("https://kupis.konkuk.ac.kr/sugang/login/loginFset.jsp")

now = datetime.now()
options = Options()
options.headless = False


# executable_path 부분에 브라우저 드라이버 파일 경로를 입력
driver = webdriver.Chrome(
    executable_path='C:/Users/thsxo/OneDrive/utility/chromedriver.exe', options=options)
wait = WebDriverWait(driver, 10)
driver.get(URL)


def login():

    frame = wait.until(EC.element_to_be_clickable(
        (By.TAG_NAME, 'frame')))

    driver.switch_to.frame(frame)
    # driver.swi

    loginBtn = driver.find_element_by_xpath(
        '//html/head')

    # /html/body/form/table/tbody/tr/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td[3]/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/img

    id_box = driver.find_element_by_css_selector('input[type="text"]')
    pw_box = driver.find_element_by_css_selector('input[type="password"]')

    # id_box.click()
    # pyperclip.copy(ID)
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys(
    #     'v').key_up(Keys.CONTROL).perform()

    # pw_box.click()
    # pyperclip.copy(PW)
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys(
    #     'v').key_up(Keys.CONTROL).perform()

    id_box.click()
    id_box.send_keys(ID)
    pw_box.click()
    pw_box.send_keys(PW)

    login = driver.find_element_by_css_selector(
        'td[rowspan="2"]').click()


def main():

    login()


if __name__ == "__main__":
    main()
