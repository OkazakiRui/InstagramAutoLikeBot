from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# IDとパスワード
username = "taisei3040"
password = "Rui200226"
# いいねの回数 (nice_num * taglist.length)
nice_num = 1000
# ランダムにしたい場合は
# nice_num = random.randint(最小値, 最大値)
# taglist = ['過去pic']
# taglist = ['フォロー大歓迎']
# taglist = ['美男美女と繋がりたい']
taglist = ['雰囲気好きな人いいね']

def randomDelay():
    time.sleep(random.randint(1, 5))

def login():
    # login page
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(1)
    driver.find_element_by_name('username').send_keys(username)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(1)

	#ログインボタンを押す
    driver.find_element_by_class_name('L3NKy').click()
    randomDelay()

# hash tag search
def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    randomDelay()

def clicknice(nice_num):
    randomDelay()
    driver.execute_script("window.scrollTo(0, 600);")
    randomDelay()
    # 最初の9枚は人気のある投稿のためスキップ
    target = driver.find_elements_by_class_name('_9AhH0')[10]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    time.sleep(1)

    # 投稿click ( モーダルopen )
    driver.find_elements_by_class_name('_9AhH0')[9].click()
    randomDelay()
    # いいねボタン
    driver.find_element_by_class_name('fr66n').click()

    for i in range(nice_num-1):
        # 次の投稿へ移動
        driver.find_element_by_css_selector('.l8mY4 .wpO6b').click()
        randomDelay()
        time.sleep(1)

        # いいねを押す
        driver.find_element_by_class_name('fr66n').click()
        randomDelay()

if __name__ == '__main__':
    driver = webdriver.Chrome("./chromedriver")
    time.sleep(1)
    login()
    randomDelay()

    # ↓タグリストをランダムで回す
    # tagsearch(random.choice(taglist))
    for tag in taglist:
        tagsearch(tag)
        clicknice(nice_num)

    driver.quit()