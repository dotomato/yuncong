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

def getname(id):
    url = BASE_URL + '/get_info_by_student_id?student_id=' + str(id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload['name']


def get_info_by_id(_id):
    url = BASE_URL + '/get_info?id=' + str(_id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload

def click_label_yy1():
    win.l1.show()
    win.l2.show()
    win.l3.show()
    win.l4.show()
    win.lyy1.hide()
    win.lyy2.hide()
    win.bg.setPixmap(win.p1)
    QApplication.processEvents()


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
        win.bg.setPixmap(win.yyqr)
        nnn = get_info_by_id(str(r[1]))['name']
        tts('您好'+nnn+'请取餐。')
        playaudio()
        QApplication.processEvents()

        time.sleep(3)
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









def click_label_1():
    win.l1.hide()
    win.l2.hide()
    win.l3.hide()
    win.l4.hide()
    win.l5.show()
    win.bg.setPixmap(win.jk)
    QApplication.processEvents()


def click_label_2():
    win.l5.hide()
    win.bg.setPixmap(win.p2)
    QApplication.processEvents()
    win.camera.capture('img.jpg')
    group = 'cj'
    img = open('img.jpg', 'rb').read()
    r = face_identify(group, img)
    if r[0] == True:
        win.result.show()
        win.bg.setPixmap(win.p3)
        nnn = get_info_by_id(str(r[1]))['name']
        win.result.setText('您好'+nnn+'，此次消费 14 元。')
        tts('您好'+nnn+'，此次消费 14 元。')
        playaudio()
        QApplication.processEvents()

        time.sleep(3)
        win.bg.setPixmap(win.yybg)
        win.lyy1.show()
        win.lyy2.show()
        win.result.hide()
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
        self.l1.mousePressEvent = self.click_label_1
        self.l2.mousePressEvent = self.click_label_1
        self.l3.mousePressEvent = self.click_label_1
        self.l4.mousePressEvent = self.click_label_1
        self.l5.mousePressEvent = self.click_label_2
    def click_label_yy1(self,gg):
        click_label_yy1()
    def click_label_yy2(self,gg):
        click_label_yy2()
    def click_label_1(self,gg):
        click_label_1()
    def click_label_2(self,gg):
        click_label_2()
    def click_exit(self,gg):
        qApp.quit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main_Ui()
    win.showFullScreen()
    sys.exit(app.exec_())

