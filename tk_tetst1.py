#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tk_tetst1.py
@time: 2018/12/31 16:25
@desc: 建立tk界面
"""

import tkinter as tk
import yinyangshi.setting as sett
import yinyangshi.parameters as par
import yinyangshi.baigui_test as ghost1
import yinyangshi.douji_test as douji1
import yinyangshi.hunshi_test2 as hunshi1
import yinyangshi.xiezuo_test as xiezuo1
from threading import Thread
import sys
import os
import pythoncom
import pyHook
import gc

root = tk.Tk()
root.title("李英俊超级无敌痒痒鼠脚本！")
root.geometry(par.left_up_loc)

# 窗口不可变
root.resizable(0, 0)


def hunshi_r():
    print('**********魂十脚本开始**********')
    t1 = Thread(target=hunshi1.run)
    t2 = Thread(target=ghost1.hook)
    # t3 = Thread(target=xiezuo1.run)
    #
    # t3.start()
    t2.start()
    t1.start()


def douji():
    print('**********斗技脚本开始**********')
    t1 = Thread(target=douji1.run)
    t2 = Thread(target=ghost1.hook)
    # t3 = Thread(target=xiezuo1.run)
    #
    # t3.start()
    t2.start()
    t1.start()


def baigui():
    print('**********百鬼脚本开始**********')
    t1 = Thread(target=ghost1.run)
    t2 = Thread(target=ghost1.hook)
    # t3 = Thread(target=xiezuo1.run)
    #
    # t3.start()
    t2.start()
    t1.start()


def quit():
    os._exit(0)


frame = tk.Frame(root, width=200, height=200)
frame.pack()
quitButton = tk.Button(frame, text='退出', command=quit, height=2, width=10).grid(row=1, column=0)
baigui = tk.Button(frame, text='百鬼夜行', command=baigui, height=2, width=10).grid(row=0, column=0)
douji = tk.Button(frame, text='斗技', command=douji, height=2, width=10).grid(row=0, column=1)
hunshi_r = tk.Button(frame, text='魂十（被邀）', command=hunshi_r, height=2, width=10).grid(row=0, column=2)

tk.mainloop()
