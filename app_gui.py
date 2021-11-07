from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import tkinter
import app_gui_script

def start():
    if loginId_txt.get() != '':
        username = loginId_txt.get()
    else:
        print('Login IDが入力されていません。')
        return

    if password_txt.get() != '':
        password = password_txt.get()
    else:
        print('Passwordが入力されていません。')
        return


    if nice_num_txt.get() != '':
        nice_num = int(nice_num_txt.get())
    else:
        nice_num_txt.insert(tkinter.END,"900")
        nice_num = int(nice_num_txt.get())

    if checkbox.get():
        interval = -1
    else:
        if interval_txt.get() != '':
            interval = int(interval_txt.get())
        else:
            interval_txt.insert(tkinter.END,"40")
            interval = int(interval_txt.get())


    # ハッシュタグを配列に格納
    taglist = []
    for tn in range(TAG_NUM):
        if tag_txt[tn].get() != '':
            taglist.append(tag_txt[tn].get())
    if len(taglist) == 0:
        print('ハッシュタグが入力されていません。')
        return

    print('ユーザーネーム：%s' % username)
    print('最大いいね回数：%d回' % nice_num)
    print('いいね間隔：%d秒' % interval)
    print(taglist)

    # いいねの回数(いいね最大回数をタグ数に平等に分ける)
    nice_num = int(nice_num / len(taglist))

    driver = webdriver.Chrome("./chromedriver")
    time.sleep(1)

    app_gui_script.login(driver, username, password)

    for tag in taglist:
        app_gui_script.tagsearch(driver, tag)
        app_gui_script.clicknice(driver, nice_num, interval)
    print("いいね完了！")

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('InstagramAutoLikeBot')
    root.geometry('450x370')

    # 座標
    FORM_X = 20
    FORM_Y = 38
    PARAM_X = 20
    PARAM_Y = 100
    START_X = 20
    START_Y = 300
    TAG_X = 260
    TAG_Y = 20

    # ログイン
    loginId_lbl = tkinter.Label(text='Login Id')
    loginId_lbl.place(x=FORM_X, y=FORM_Y)
    loginId_txt = tkinter.Entry(width=13)
    loginId_txt.place(x=FORM_X+100, y=FORM_Y)
    password_lbl = tkinter.Label(text='Password')
    password_lbl.place(x=FORM_X, y=FORM_Y+30)
    password_txt = tkinter.Entry(width=13, show='*')
    password_txt.place(x=FORM_X+100, y=FORM_Y+30)

    # パラメータ項目
    nice_num_lbl = tkinter.Label(text='最大いいね回数')
    nice_num_lbl.place(x=PARAM_X, y=PARAM_Y)
    nice_num_txt = tkinter.Entry(width=10)
    nice_num_txt.place(x=PARAM_X+100, y=PARAM_Y)
    nice_numU_lbl = tkinter.Label(text='回')
    nice_numU_lbl.place(x=PARAM_X+200, y=PARAM_Y+5)
    interval_lbl = tkinter.Label(text='いいね間隔')
    interval_lbl.place(x=PARAM_X, y=PARAM_Y+30)
    interval_txt = tkinter.Entry(width=10)
    interval_txt.place(x=PARAM_X+100, y=PARAM_Y+30)
    intervalU_lbl = tkinter.Label(text='秒')
    intervalU_lbl.place(x=PARAM_X+200, y=PARAM_Y+35)

    # chekbox
    checkbox = tkinter.BooleanVar()
    like_random_interval = tkinter.Checkbutton(text='いいね間隔をランダムにする', variable=checkbox)
    like_random_interval.place(x=PARAM_X, y=PARAM_Y+60)

    # ハッシュタグ
    hashTag_lbl = tkinter.Label(text='ハッシュタグ')
    hashTag_lbl.place(x=TAG_X, y=TAG_Y)
    TAG_NUM = 10
    tag_txt = []
    for tn in range(TAG_NUM):
        tag_txt.append(tkinter.Entry(width=15))
        tag_txt[tn].place(x=TAG_X+10, y=TAG_Y+30*(tn+1))

    # 開始ボタン
    start_btn = tkinter.Button(root, text='Start', command=start)
    start_btn.place(x=START_X, y=START_Y)
    
    # メインループ
    root.mainloop()