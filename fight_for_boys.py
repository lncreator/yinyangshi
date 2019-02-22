#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: fight_for_boys.py
@time: 2019/1/16 20:05
@desc: 为崽而战脚本测试1
"""

import pyautogui as ptg
import time
from threading import Thread
import yinyangshi.parameters as par
import yinyangshi.setting as sett
from yinyangshi.baigui_test import click_motion, just_motion, click_small
from yinyangshi.random_file import *
import yinyangshi.baigui_test as ghost1


def run_start():
    """最开始的界面"""
    while sett.state:
        # 点击开始斗技
        sett.ffb_start = ptg.pixelMatchesColor(par.ffb_start_loc[0], par.ffb_start_loc[1], par.ffb_start_color)

        if sett.ffb_start and sett.state:
            # 开始战斗
            click_motion(par.ffb_start_loc)
            time.sleep(pause_time() + 1)

        time.sleep(pause_time())


def run1():
    """选式神界面，banpick"""
    while sett.state:
        # 自动上阵
        sett.banpick_state = ptg.pixelMatchesColor(par.zidongshang_loc[0], par.zidongshang_loc[1], par.zidongshang_color)

        if sett.banpick_state and sett.state:
            # 现在是高段位的banpick阶段
            # 点击自动上场
            click_small(par.zidongshang_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)
            time.sleep(pause_time() + 1)

        time.sleep(pause_time())


def run2():
    """或者是是准备的那种界面，不用自动上阵，点准备就好了"""
    while sett.state:
        # 点击准备
        sett.waiting_state = ptg.pixelMatchesColor(par.zhunbei_state_loc[0], par.zhunbei_state_loc[1], par.zhunbei_state_color)

        if sett.waiting_state and sett.state:
            # 如果没有自动上场界面的话，就是手动准备
            # 点击准备
            click_motion(par.zhunbei_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)
            time.sleep(pause_time() + 1)

        time.sleep(pause_time())


def run3():
    """所有式神上阵好了之后，这时候需要点自动（不点也可以哈哈哈）,所以这里要检测手动"""
    while sett.state:
        # 点击自动
        sett.shoudong = ptg.pixelMatchesColor(par.shoudong_loc[0], par.shoudong_loc[1], par.shoudong_color)

        if sett.shoudong and sett.state:
            # 准备之后需要把手动变成自动
            # 点击手动
            click_motion(par.shoudong_click)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

            time.sleep(pause_time() + 1)

        time.sleep(pause_time())


def run4():
    """监测获胜与否"""
    while sett.state:
        # 获胜了点一下
        sett.shibai = ptg.pixelMatchesColor(par.ffb_lose[0], par.ffb_lose[1], par.ffb_lose_color)
        sett.shengli = ptg.pixelMatchesColor(par.ffb_win_loc[0], par.ffb_win_loc[1], par.ffb_win_color)

        if sett.shengli or sett.shibai:
            # 战斗结束
            click_motion(par.ffb_lose)
            sett.number += 1
            just_motion(par.rr_loc)
            print('完成第' + str(sett.number) + '次斗技。。。')

            time.sleep(pause_time() + 3)

        time.sleep(pause_time())


def main():
    """主程序"""
    threads_list = []
    ts = Thread(target=run_start)
    threads_list.append(ts)
    t1 = Thread(target=run1)
    threads_list.append(t1)
    t2 = Thread(target=run2)
    threads_list.append(t2)
    t3 = Thread(target=run3)
    threads_list.append(t3)
    t4 = Thread(target=run4)
    threads_list.append(t4)
    th = Thread(target=ghost1.hook)
    threads_list.append(th)

    for i in threads_list:
        i.start()
    for j in threads_list:
        j.join()


if __name__ == '__main__':
    main()