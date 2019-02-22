#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: hunshi_test3.py
@time: 2019/1/12 20:20
@desc: 魂十测试3
"""

import pyautogui as ptg
import time
import gc
from threading import Thread
import yinyangshi.parameters as par
import yinyangshi.setting as sett
from yinyangshi.baigui_test import click_motion, just_motion, click_small
from yinyangshi.random_file import *
import yinyangshi.baigui_test as ghost1
import yinyangshi.fight_for_boys as ffb


def yaoqing1():
    """接收邀请和自动邀请"""
    while sett.state:
        sett.yaoqing1 = ptg.pixelMatchesColor(par.hs_yaoqing_loc[0], par.hs_yaoqing_loc[1], par.hs_yaoqing_color)

        if sett.yaoqing1:
            click_small(par.hs_yaoqing_loc)
            time.sleep(pause_time() + 2)

        time.sleep(pause_time())


def yaoqing2():
    """接收邀请和自动邀请"""
    while sett.state:
        sett.yaoqing2 = ptg.pixelMatchesColor(par.hunshi_yaoqing_loc[0], par.hunshi_yaoqing_loc[1], par.hunshi_yaoqing_color)

        if sett.yaoqing2:
            click_small(par.hunshi_yaoqing_loc)
            time.sleep(pause_time() + 2)

        time.sleep(pause_time())


def run1():
    # 主循环
    while sett.state:
        # 接受别人邀请的人，只需要点击结算界面
        # 监测胜利还是失败
        sett.hunshi_win = ptg.pixelMatchesColor(par.hunshi_loc[0], par.hunshi_loc[1], par.hunshi_color)

        if sett.hunshi_win and sett.state:
            # 战斗结束
            # 点击领取奖励
            click_motion(par.hunshi_loc)
            time.sleep(pause_time())
            click_motion(par.hunshi_loc)

            time.sleep(pause_time()+2)

        time.sleep(pause_time())


def run2():
    # 主循环
    while sett.state:
        sett.hs_jiesuan = ptg.pixelMatchesColor(par.hs_jiesuan_loc[0], par.hs_jiesuan_loc[1], par.hs_jiesuan_color)

        if sett.hs_jiesuan and sett.state:
            # 领取奖励
            # 点击返回
            time.sleep(pause_time()+2)
            sett.number += 1
            click_motion(par.hunshi_loc)
            time.sleep(pause_time())
            click_motion(par.hunshi_loc)
            time.sleep(pause_time())
            click_motion(par.hunshi_loc)

            time.sleep(pause_time()+3)

            # 魂十刷完了
            print('完成第' + str(sett.number) + '次魂十。。。')

        time.sleep(pause_time())


def main():
    gc.enable()
    threads_list = []
    t1 = Thread(target=run1)
    threads_list.append(t1)
    t2 = Thread(target=run2)
    threads_list.append(t2)
    t3 = Thread(target=yaoqing2)
    threads_list.append(t3)
    t4 = Thread(target=yaoqing1)
    threads_list.append(t4)
    th = Thread(target=ghost1.hook)
    threads_list.append(th)

    # t5 = Thread(target=ffb.run2)
    # threads_list.append(t5)

    for i in threads_list:
        i.start()
    for j in threads_list:
        j.join()


if __name__ == '__main__':
    main()