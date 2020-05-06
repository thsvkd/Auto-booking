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
URL = ("http://www.cgv.co.kr/")

now = datetime.now()
options = Options()
options.headless = False

# executable_path 부분에 브라우저 드라이버 파일 경로를 입력
driver = webdriver.Chrome(
    executable_path='C:/Users/thsxo/OneDrive/utility/chromedriver.exe',
    options=options)
wait = WebDriverWait(driver, 10)
driver.get(URL)


def login():

    loginBtn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[class="login"]'))).click()

    id_box = driver.find_element_by_id('txtUserId')
    pw_box = driver.find_element_by_id('txtPassword')

    id_box.click()
    pyperclip.copy(ID)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(
        Keys.CONTROL).perform()

    pw_box.click()
    pyperclip.copy(PW)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(
        Keys.CONTROL).perform()

    # id_box.click()
    # id_box.send_keys(ID)
    # pw_box.click()
    # pw_box.send_keys(PW)

    login = driver.find_element_by_css_selector(
        'button[type="submit"]').click()

    try:
        wait.until(
            EC.element_to_be_clickable(
                (By.ID,
                 'ctl00_PlaceHolderContent_btn_pw_chag_later'))).click()
    except:
        print('skip pw change\n')

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/ticket/"]'))).click()

    iframe = wait.until(EC.element_to_be_clickable((By.ID, 'ticket_iframe')))

    driver.switch_to.frame(iframe)

    movie_table = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'ul[class="content scroll-y"]')))

    #wait = WebDriverWait(movie_table, 10)

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-index="0"]')))

    # time.sleep(1)

    movie_list = movie_table.find_elements_by_tag_name('li')

    # print(movie_table.text)

    for i, item in enumerate(movie_list):
        print(str(i) + " " + item.text)

    print('보고싶은 영화를 선택하세요 : ')
    sel_movie = input()

    if str(type(sel_movie)) == "<class 'int'>":
        sel_movie = movie_list[int(sel_movie)]
        print('sel' + sel_movie.text)
    else:
        for i, item in enumerate(movie_list):
            if sel_movie in item.text:
                print(item.text)
                sel_movie = item

                break

    print('selection fin\n')
    sel_movie.click()

    theater_list = driver.find_element_by_css_selector(
        'div[class="theater-list"]')
    area = theater_list.find_element_by_id('theater_area_list')
    area = area.find_elements_by_tag_name('li')

    point = driver.find_element_by_css_selector(
        'div[class="area_theater_list nano has-scrollbar has-scrollbar-y"]')
    point = point.find_elements_by_tag_name('li')

    a = 1


def main():

    login()


if __name__ == "__main__":
    main()
