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
ID = "xxxx"
PW = "xxxx"
URL = "https://booking.naver.com/booking/6/bizes/230889"

now = datetime.now()
options = Options()
options.headless = False

# executable_path 부분에 브라우저 드라이버 파일 경로를 입력
driver = webdriver.Chrome(
    executable_path='C:/Users/thsxo/OneDrive/utility/chromedriver.exe',
    options=options)
wait = WebDriverWait(driver, 10)
driver.get(URL)
# time.sleep(5)

# 로그인 함수
# 아이디 창과 패스워드 입력 창을 찾아서 클릭할 수 있을때까지 기다린 다음 자동으로 입력을 합니다


def login():

    loginBtn = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "gnb_btn_login"))).click()

    id_box = wait.until(EC.element_to_be_clickable((By.ID, "id")))
    pw_box = driver.find_element_by_id("pw")

    id_box.click()
    pyperclip.copy(ID)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(
        Keys.CONTROL).perform()

    pw_box.click()
    pyperclip.copy(PW)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(
        Keys.CONTROL).perform()

    login = wait.until(EC.element_to_be_clickable(
        (By.ID, "log.login"))).click()

    time.sleep(0.5)


def wait_booking():
    booking_btn = 0

    while True:

        try:
            print("try")
            more_info = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'span[ng-bind-html="bizItemInfo.name | newlines"]')))
            booking_btn = driver.find_element_by_css_selector(
                'span[ng-bind-html="bizItemInfo.name | newlines"]')
        except:
            driver.refresh()
            print("refresh")
            time.sleep(0.5)
        if booking_btn != 0:
            break

    booking_btn.click()


def get_calender():

    calendar = wait.until(EC.element_to_be_clickable((By.ID, "calendar")))

    month = calendar.find_element_by_css_selector(
        'span[ng-bind="$ctrl.baseDate.get(\'month\') + 1"]')

    print(month.text)

    nobth_sel_btn_R = calendar.find_element_by_css_selector(
        'a[ng-click="$ctrl.nextMonth()"]')
    nobth_sel_btn_L = calendar.find_element_by_css_selector(
        'a[ng-click="$ctrl.prevMonth()"]')

    if month.text == str(now.month):
        nobth_sel_btn_R.click()

    return calendar


def make_booking(calendar):

    # wait.until(
    #     EC.text_to_be_present_in_element(
    #         (By.CSS_SELECTOR, 'span[ng-bind="$ctrl.getDay(key)"]'), "12"))

    time.sleep(0.5)

    calendar_table = calendar.find_element_by_class_name("tb_body")
    weeks = calendar_table.find_elements_by_tag_name("tr")

    sat_date = []
    sun_date = []
    etc_date = []

    for item in weeks:
        days = item.find_elements_by_tag_name("td")
        for item2 in days:
            class_attribute = item2.get_attribute("class")
            if class_attribute == "calendar-sat":
                sat_date.append(item2)
            elif class_attribute == "calendar-sun":
                sun_date.append(item2)
            else:
                etc_date.append(item2)

    sat_date[1].click()

    ###
    time.sleep(0.1)
    customer_selector = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "customer_selector")))
    time_select_am = customer_selector.find_element_by_css_selector(
        'div[class="am"]'
    ).find_elements_by_css_selector('span[ng-bind="$ctrl.getStartTime(timeSchedule)"]')
    time_select_pm = customer_selector.find_element_by_css_selector(
        'div[class="pm"]'
    ).find_elements_by_css_selector('span[ng-bind="$ctrl.getStartTime(timeSchedule)"]')

    time_select = [time_select_am, time_select_pm]

    time_select[1][0].click()

    agree_btn = driver.find_element_by_xpath(
        "//div[@class='section_booking_agreement']/div[@class='agreement all']/label"
    ).click()
    gogo_btn = driver.find_element_by_css_selector(
        "button[ng-click='$ctrl.clickSubmit($event)']").click()

    pop_up = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'div[class="popup_booking application notify app_notice confirm_type"]'
        )))

    if pop_up.text.split('\n')[0] == "예약이 확정되었습니다.":
        print("success!!\n")
        return 1
    else:
        print("fail..\n")
        return 0


def main():

    result = 0

    login()
    wait_booking()
    calendar = get_calender()

    while result != 1:
        result = make_booking(calendar)


if __name__ == "__main__":
    main()
