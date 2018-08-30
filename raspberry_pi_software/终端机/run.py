# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from progui import *
import time
import picamera
from yuncongclientlib import *
import sys


import pygame
def playaudio():
    file=r'audio.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()

import urllib.request
import urllib.parse
import json

BASE_URL = 'http://vps4.1994.io:5000'
REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    }

j1 = 0
j2 = 0
j3 = 0
j4 = 0

def click_j1():
    global j1
    if j1 == 0:
        print('------------------>1')

        j1 = 1
        win.jk1.setPixmap(win.x11)
    if j1 == 1:
        print('------------------>0')

        j1 = 0
        win.jk1.setPixmap(win.x10)
def click_j2():
    global j2
    if j2 == 0:

        j2 = 1
        win.jk2.setPixmap(win.x21)
    if j2 == 1:

        j2 = 0
        win.jk2.setPixmap(win.x20)
def click_j3():
    global j3
    if j3 == 0:

        j3 = 1
        win.jk3.setPixmap(win.x31)
    if j3 == 1:

        j3 = 0
        win.jk3.setPixmap(win.x30)
def click_j4():
    global j4
    if j4 == 0:

        j4 = 1
        win.jk4.setPixmap(win.x41)
    if j4 == 1:

        j4 = 0
        win.jk4.setPixmap(win.x40)


def get_info_by_yuncong_id(_id):
    url = BASE_URL + '/get_info_by_yuncong_id?yuncong_id=' + str(_id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload

def get_number(_id):
    url = BASE_URL + '/get_number?student_id=' + str(_id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload
def get_recommend(_id):
    url = BASE_URL + '/get_recommend?student_id=' + str(_id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload
def get_food(name):
    url = BASE_URL + '/get_food?name=' + str(name)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload
def add_book_instant(student_id,machine,food,hall,jiko):
    url = BASE_URL + '/add_book_instant?student_id=' + str(student_id)+'&machine='+str(machine)+'&food='+str(food)+'&hall='+str(hall)+'&jiko='+str(jiko)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload
dc_food = ""
dc_name = ""
dc_student_id = ""
dc_money = 0
dc_cost = 0
dc_tj = ""

def click_label_yy1():
    win.lyy1.hide()
    win.lyy2.hide()
    win.bg.setPixmap(win.p2)
    QApplication.processEvents()
    win.camera.capture('img.jpg')
    group = 'cj'
    img = open('img.jpg', 'rb').read()
    r = face_identify(group, img)
    if r[0] == True:
        ycid = r[1]
        info = get_info_by_yuncong_id(ycid)
        global dc_name
        global dc_student_id
        global dc_money
        dc_name = info['name']
        dc_student_id = str(info['student_id'])
        dc_money = info['money']
        book_r = get_number(dc_student_id)
        win.bg.setPixmap(win.p1)
        win.l1.show()
        win.l2.show()
        win.l3.show()
        win.l4.show()
        win.l1.setPixmap(win.b1)
        win.l2.setPixmap(win.b2)
        win.l3.setPixmap(win.b3)
        global dc_tj
        dc_tj = get_recommend(dc_student_id)['name']
        win.l4.setText('为您独家推荐: '+dc_tj)
        QApplication.processEvents()
        tts('您好'+dc_name+'，请点餐！')
        playaudio()
    else:
        win.result.show()
        win.bg.setPixmap(win.p2)
        win.result.setText('识别失败 请重试')
        tts('识别失败 请重试')
        playaudio()
        QApplication.processEvents()
        time.sleep(3)
        win.bg.setPixmap(win.yybg)
        win.lyy1.show()
        win.lyy2.show()
        win.result.hide()


def click_label_yy2():
    win.lyy1.hide()
    win.lyy2.hide()
    win.bg.setPixmap(win.p2)
    QApplication.processEvents()
    win.camera.capture('img.jpg')
    group = 'cj'
    img = open('img.jpg', 'rb').read()
    r = face_identify(group, img)
    if r[0] == True:
        ycid = r[1]
        info = get_info_by_yuncong_id(ycid)
        name = info['name']
        student_id = info['student_id']
        book_r = get_number(student_id)
        if book_r == {}:
            win.result.show()
            win.bg.setPixmap(win.p2)
            win.result.setText('您没有预约信息！')
            tts('您没有预约信息！')
            playaudio()
            QApplication.processEvents()
            time.sleep(3)
            win.bg.setPixmap(win.yybg)
            win.lyy1.show()
            win.lyy2.show()
            win.result.hide()

        else:
            win.bg.setPixmap(win.yyqr)
            foodnum = book_r['number']





            tts('您好'+name+'请于食品柜'+str(foodnum)+'号取餐。')
            playaudio()
            win.jk1.show()
            win.jk2.show()
            win.jk3.show()
            win.jk4.show()
            win.food.show()
            win.jk1.setPixmap(win.x10)
            win.jk2.setPixmap(win.x20)
            win.jk3.setPixmap(win.x30)
            win.jk4.setPixmap(win.x40)
            if '免辣' in book_r['jiko']:
                win.jk1.setPixmap(win.x11)
            if '免葱' in book_r['jiko']:
                win.jk2.setPixmap(win.x21)
            if '免香菜' in book_r['jiko']:
                win.jk3.setPixmap(win.x31)
            if '免汁' in book_r['jiko']:
                win.jk4.setPixmap(win.x41)

            win.food.setText(book_r['food']+' 位于 '+str(foodnum)+'号食品柜')
            QApplication.processEvents()

            time.sleep(5)
            win.jk1.hide()
            win.jk2.hide()
            win.jk3.hide()
            win.jk4.hide()
            win.food.hide()
            win.bg.setPixmap(win.yybg)
            win.lyy1.show()
            win.lyy2.show()
    else:
        win.result.show()
        win.bg.setPixmap(win.p2)
        win.result.setText('识别失败 请重试')
        tts('识别失败 请重试')
        playaudio()
        QApplication.processEvents()
        time.sleep(3)
        win.bg.setPixmap(win.yybg)
        win.lyy1.show()
        win.lyy2.show()
        win.result.hide()









def click_food_1():
    win.l1.hide()
    win.l2.hide()
    win.l3.hide()
    win.l4.hide()
    win.l5.show()
    win.food.show()
    win.food.setPixmap(win.b1)
    global dc_food
    dc_food = "木须肉"
    win.bg.setPixmap(win.jk)
    win.jk1.show()
    win.jk1.setPixmap(win.x10)
    global j1
    j1 = 0
    win.jk2.show()
    win.jk2.setPixmap(win.x20)
    global j2
    j2 = 0
    win.jk3.show()
    win.jk3.setPixmap(win.x30)
    global j3
    j3 = 0
    win.jk4.show()
    win.jk4.setPixmap(win.x40)
    global j4
    j4 = 0
    QApplication.processEvents()


def click_food_2():
    win.l1.hide()
    win.l2.hide()
    win.l3.hide()
    win.l4.hide()
    win.l5.show()
    win.food.show()
    win.food.setPixmap(win.b2)
    global dc_food
    dc_food = "小炒肉"
    win.bg.setPixmap(win.jk)
    win.jk1.show()
    win.jk1.setPixmap(win.x10)
    global j1
    j1 = 0
    win.jk2.show()
    win.jk2.setPixmap(win.x20)
    global j2
    j2 = 0
    win.jk3.show()
    win.jk3.setPixmap(win.x30)
    global j3
    j3 = 0
    win.jk4.show()
    win.jk4.setPixmap(win.x40)
    global j4
    j4 = 0
    QApplication.processEvents()

def click_food_3():
    win.l1.hide()
    win.l2.hide()
    win.l3.hide()
    win.l4.hide()
    win.l5.show()
    win.food.show()
    win.food.setPixmap(win.b3)
    global dc_food
    dc_food = "手撕包菜"
    win.bg.setPixmap(win.jk)
    win.jk1.show()
    win.jk1.setPixmap(win.x10)
    global j1
    j1 = 0
    win.jk2.show()
    win.jk2.setPixmap(win.x20)
    global j2
    j2 = 0
    win.jk3.show()
    win.jk3.setPixmap(win.x30)
    global j3
    j3 = 0
    win.jk4.show()
    win.jk4.setPixmap(win.x40)
    global j4
    j4 = 0
    QApplication.processEvents()


def click_food_4():
    win.l1.hide()
    win.l2.hide()
    win.l3.hide()
    win.l4.hide()
    win.l5.show()
    win.food.show()
    win.food.setText(dc_tj)
    global dc_food
    dc_food = dc_tj
    win.bg.setPixmap(win.jk)
    win.jk1.show()
    win.jk1.setPixmap(win.x10)
    global j1
    j1 = 0
    win.jk2.show()
    win.jk2.setPixmap(win.x20)
    global j2
    j2 = 0
    win.jk3.show()
    win.jk3.setPixmap(win.x30)
    global j3
    j3 = 0
    win.jk4.show()
    win.jk4.setPixmap(win.x40)
    global j4
    j4 = 0
    QApplication.processEvents()






def click_label_2():
    win.l5.hide()
    win.food.hide()
    win.jk1.hide()
    win.jk2.hide()
    win.jk3.hide()
    win.jk4.hide()
    win.bg.setPixmap(win.p3)
    win.result.show()
    win.info.show()
    QApplication.processEvents()
    global dc_name
    global dc_food
    global dc_money
    global dc_cost
    global dc_student_id
    jjkk = ""
    global j1
    global j2
    global j3
    global j4
    if j1 == 1:
        jjkk = jjkk + '免辣'
    if j2 == 1:
        jjkk = jjkk + '免葱'
    if j3 == 1:
        jjkk = jjkk + '免香菜'
    if j4 == 1:
        jjkk = jjkk + '免汁'
    print(dc_food)
    print(jjkk)
    print(dc_name)
    print(dc_student_id)
    print(dc_money)
    dc_cost = get_food(dc_food)['cost']
    print(dc_cost)
    if float(dc_money) >= int(dc_cost):
        add_book_instant(dc_student_id,'25',dc_food,'西区一食堂',jjkk)
        win.result.setText('您好'+dc_name+'，此次消费 '+str(dc_cost)+' 元。')
        win.info.setText('您好'+dc_name+'，此次消费 '+str(dc_cost)+' 元。')
        QApplication.processEvents()
        tts('您好'+dc_name+'，此次消费 '+str(dc_cost)+' 元。')
        playaudio()
    else:
        win.result.setText('余额不足，请重试！')
        win.info.setText('')
        QApplication.processEvents()
        tts('余额不足，请重试！')
        playaudio()

    time.sleep(5)
    win.bg.setPixmap(win.yybg)
    win.lyy1.show()
    win.lyy2.show()
    win.info.setText('')
    win.result.hide()
    win.info.hide()


class Main_Ui(QWidget,Ui_Dialog):
    def __init__(self,parent=None):
        super(Main_Ui,self).__init__(parent)
        self.setupUi(self)
        self.p1 = QPixmap(":p1.png")
        self.p2 = QPixmap(":p2.png")
        self.p3 = QPixmap(":p3.png")
        self.b1 = QPixmap(":b1.png")
        self.b2 = QPixmap(":b2.png")
        self.b3 = QPixmap(":b3.png")
        self.b5 = QPixmap(":b5.png")
        self.jk = QPixmap(":jk.png")
        self.yyqr = QPixmap(":yyqr.png")
        self.yyb1 = QPixmap(":yyb1.png")
        self.yyb2 = QPixmap(":yyb2.png")
        self.yybg = QPixmap(":yybg.png")
        self.x10 = QPixmap(":x10.png")
        self.x11 = QPixmap(":x11.png")
        self.x20 = QPixmap(":x20.png")
        self.x21 = QPixmap(":x21.png")
        self.x30 = QPixmap(":x30.png")
        self.x31 = QPixmap(":x31.png")
        self.x40 = QPixmap(":x40.png")
        self.x41 = QPixmap(":x41.png")
        self.ck = QPixmap(":ck.png")
        self.quit = QPixmap(":quit.png")
        self.resize(self.p1.size())
        self.setMask(self.p1.mask())
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1024, 1024)
        self.camera.start_preview(fullscreen=False,window=(5,80,350,350))
        self.bg.setPixmap(self.yybg)
        self.l1.setPixmap(self.b1)
        self.l2.setPixmap(self.b2)
        self.l3.setPixmap(self.b3)
        self.l4.setPixmap(self.b1)
        self.l5.setPixmap(self.b5)
        self.exit.setPixmap(self.quit)
        self.lyy1.setPixmap(self.yyb1)
        self.lyy2.setPixmap(self.yyb2)
        self.l5.hide()
        self.l1.hide()
        self.l2.hide()
        self.l3.hide()
        self.l4.hide()
        self.jk1.hide()
        self.jk2.hide()
        self.jk3.hide()
        self.jk4.hide()
        self.food.hide()
        self.info.hide()
        self.exit.mousePressEvent = self.click_exit
        self.lyy1.mousePressEvent = self.click_label_yy1
        self.lyy2.mousePressEvent = self.click_label_yy2
        self.l1.mousePressEvent = self.click_food_1
        self.l2.mousePressEvent = self.click_food_2
        self.l3.mousePressEvent = self.click_food_3
        self.l4.mousePressEvent = self.click_food_4
        self.l5.mousePressEvent = self.click_label_2
        self.jk1.mousePressEvent = self.click_j1
        self.jk2.mousePressEvent = self.click_j2
        self.jk3.mousePressEvent = self.click_j3
        self.jk4.mousePressEvent = self.click_j4
    def click_label_yy1(self,gg):
        click_label_yy1()
    def click_label_yy2(self,gg):
        click_label_yy2()
    def click_food_1(self,gg):
        click_food_1()
    def click_food_2(self,gg):
        click_food_2()
    def click_food_3(self,gg):
        click_food_3()
    def click_food_4(self,gg):
        click_food_4()
    def click_label_2(self,gg):
        click_label_2()
    def click_exit(self,gg):
        qApp.quit()
    def click_j1(self,gg):
        click_j1()
    def click_j2(self,gg):
        click_j2()
    def click_j3(self,gg):
        click_j3()
    def click_j4(self,gg):
        click_j4()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main_Ui()
    win.showFullScreen()
    sys.exit(app.exec_())

