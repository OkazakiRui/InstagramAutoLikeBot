from selenium import webdriver
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

from dotenv import load_dotenv
# .envファイルの内容を読み込みます
load_dotenv()

import os

import sys

import sqlite3
import re

def login():
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    f=open('insta.txt','a')
    f.write("instagramにアクセスしました\n")
    f.close()
    time.sleep(1)
    username = "asahanemutaiyo"
    password = "Rui200226"
    driver.find_element_by_name('username').send_keys(username)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(1)

	#ログインボタンを押す
    driver.find_element_by_class_name('L3NKy       ').click()
    time.sleep(random.randint(2, 5))
    f = open('insta.txt','a')
    f.write("instagramにログインしました\n")
    f.close()
    time.sleep(1)

def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    time.sleep(random.randint(2, 10))
    f = open('insta.txt','a')
    f.write("listtagより、tagで検索を行いました\n")
    f.close()
    time.sleep(1)

def clicknice():
    target = driver.find_elements_by_class_name('_9AhH0')[9]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    f = open('insta.txt','a')
    f.write("最新の投稿まで画面を移動しました\n")
    f.close()
    time.sleep(1)

    dbname = os.environ["DBNAME"]

    try:
        driver.find_elements_by_class_name('_9AhH0')[0].click()
        time.sleep(random.randint(2, 10))
        f = open('insta.txt','a')
        f.write("投稿をクリックしました\n")
        f.close()
        time.sleep(1)
        post_text = driver.find_element_by_class_name("C4VMK")
        post_contain = post_text.find_elements_by_tag_name("span")[1].text
        post_contain_plane_format = re.sub('\s', '',post_contain)
        print(post_contain_plane_format)

        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        cur.execute('select * from instagramContents where post_content=?;', (post_contain_plane_format, ))
        print(cur.fetchall())

        #新しくいいねするものだけを処理
        if not cur.fetchall(): 
            driver.find_element_by_class_name('fr66n').click()
            f = open('insta.txt','a')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(1)
            cur.execute('INSERT INTO instagramContents(post_content) values(?)',(post_contain_plane_format, ))
            conn.commit()

        for i in range(random.randint(200, 300)):
                try:
                    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                    f = open('insta.txt','a')
                    f.write("次の投稿へ移動しました\n")
                    f.close()
                    time.sleep(random.randint(random.randint(2, 5), random.randint(10, 15)))

                except WebDriverException:
                    f = open('insta.txt','a')
                    f.write("２つ目の位置でエラーが発生しました\n")
                    f.close()
                    time.sleep(5)
                    cur.close()
                    conn.close()

                try:
                    post_text = driver.find_element_by_class_name("C4VMK")
                    post_contain = post_text.find_elements_by_tag_name("span")[1].text
                    post_contain_plane_format = re.sub('\s', '',post_contain)
                    print(post_contain_plane_format)
                    cur.execute('select * from instagramContents where post_content=?;', (post_contain_plane_format,))
                    print(cur.fetchall())
                    if not cur.fetchall(): 
                        cur.execute('INSERT INTO instagramContents(post_content) values(?)',(post_contain_plane_format, ))
                        conn.commit()
                        #新しくいいねするものだけを処理
                        driver.find_element_by_class_name('fr66n').click()
                        f = open('insta.txt','a')
                        f.write("投稿にいいねしました\n")
                        f.close()
                        time.sleep(2)
                except WebDriverException:
                    f = open('insta.txt','a')
                    f.write("3つ目の位置でエラーが発生しました\n")
                    f.close()
                    cur.close()
                    conn.close()

                print("いいね回数 : ", i+1)

        cur.close()
        conn.close()

    except WebDriverException:
        f = open('insta.txt','a')
        f.write("エラーが発生しました\n")
        f.close()

        cur.close()
        conn.close()
        return

if __name__ == '__main__':
    taglist = ['おしゃれさんと繋がりたい']
    option = Options()
    # option.add_argument('--headless') 
    driver = webdriver.Chrome("C:/Users/okazaki/Desktop/instagaramLikeBot/chromedriver.exe")
    time.sleep(1)
    login()
    tagsearch(random.choice(taglist))
    clicknice()
    driver.quit()
    sys.exit()