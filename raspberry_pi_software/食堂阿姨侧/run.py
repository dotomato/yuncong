# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from progui import *
import time

from yuncongclientlib import *
import sys



import urllib.request
import urllib.parse
import json

BASE_URL = 'http://vps4.1994.io:5000'
REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    }


uuid = ''


def getname(id):
    url = BASE_URL + '/get_info_by_student_id?student_id=' + str(id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload['name']

def finish_book(id):
    url = BASE_URL + '/finish_book?uuid=' + str(id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)




def get_book_list():
    url = BASE_URL + '/get_book_list'
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    if payload == []:
        win.l2.setText('已处理完全部点菜信息')
        win.food.setText('无新点菜')
        win.jk1.setPixmap(win.x10)
        win.jk2.setPixmap(win.x20)
        win.jk3.setPixmap(win.x30)
        win.jk4.setPixmap(win.x40)
    else:
        a = payload
        a.reverse()
        win.food.setText(a[0]['food'])
        global uuid
        uuid = a[0]['uuid']
        win.jk1.setPixmap(win.x10)
        win.jk2.setPixmap(win.x20)
        win.jk3.setPixmap(win.x30)
        win.jk4.setPixmap(win.x40)
        if '免辣' in a[0]['jiko']:
            win.jk1.setPixmap(win.x11)
        if '免葱' in a[0]['jiko']:
            win.jk2.setPixmap(win.x21)
        if '免香菜' in a[0]['jiko']:
            win.jk3.setPixmap(win.x31)
        if '免汁' in a[0]['jiko']:
            win.jk4.setPixmap(win.x41)
        t = ''
        n = 0
        for i in a:
            n += 1
            t = t + str(n) + '  ' + getname(i['student_id'])+ '  ' + i['food']+ '  ' + i['jiko'] + '\n'
        win.l2.setText(t)

def click_l1():
    global uuid
    finish_book(uuid)
    get_book_list()
    QApplication.processEvents()





















class Main_Ui(QWidget,Ui_Dialog):
    def __init__(self,parent=None):
        super(Main_Ui,self).__init__(parent)
        self.setupUi(self)
        self.p1 = QPixmap(":p1.png")
        self.b1 = QPixmap(":b1.png")
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
        self.bg.setPixmap(self.p1)
        self.l1.setPixmap(self.b1)
        self.foodbg.setPixmap(self.ck)

        self.l1.mousePressEvent = self.click_l1


        self.exit.mousePressEvent = self.click_exit

    def click_exit(self,gg):
        qApp.quit()
        os.system('pkill python3')
    def click_l1(self,gg):
        click_l1()


def looprefresh():
    while(1):
        get_book_list()
        time.sleep(10)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main_Ui()
    win.showFullScreen()
    from threading import Thread
    t=Thread(target=looprefresh)
    t.start()
    sys.exit(app.exec_())

