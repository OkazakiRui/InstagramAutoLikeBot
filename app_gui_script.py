from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def randomDelay():
    time.sleep(random.randint(2, 5))

def login(driver, username, password):
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
def tagsearch(driver, tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    randomDelay()

def clicknice(driver, nice_num, interval):
    # 最初の9枚は人気のある投稿のためスキップ
    target = driver.find_elements_by_class_name('_9AhH0')[10]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    time.sleep(1)
    # 投稿click ( モーダルopen )
    driver.find_elements_by_class_name('_9AhH0')[9].click()
    if interval == -1:
        print("random")
        randomDelay()
    else:
        time.sleep(interval)
    # いいねボタン
    driver.find_element_by_class_name('fr66n').click()
    time.sleep(1)

    for i in range(nice_num-1):
        # 次の投稿へ移動
        driver.find_elements_by_class_name('wpO6b')[2].click()
        if interval == -1:
            print("random")
            randomDelay()
        else:
            time.sleep(interval)
        
        # いいねを押す
        driver.find_element_by_class_name('fr66n').click()
        time.sleep(1)