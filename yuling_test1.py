#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: yuling_test1.py
@time: 2019/1/13 14:31
@desc:御灵打黑豹
"""


import pyautogui as ptg
import time
import gc
from threading import Thread
import yinyangshi.parameters as par
import yinyangshi.setting as sett
from yinyangshi.baigui_test import click_motion, just_motion
import yinyangshi.baigui_test as ghost1
from yinyangshi.random_file import *


def run_yuling():
    # 主循环
    while sett.state:
        # 御灵准备界面
        sett.yuling = ptg.pixelMatchesColor(par.yuling_tiaozhan_loc[0], par.yuling_tiaozhan_loc[1], par.yuling_tiaozhan_color)

        if sett.yuling:

            if not ptg.pixelMatchesColor(par.heibao_loc[0], par.heibao_loc[1], par.heibao_color):
                click_motion(par.heibao_loc)
                time.sleep(pause_time())
                just_motion(par.rr_loc)

            if not ptg.pixelMatchesColor(par.sanceng_loc[0], par.sanceng_loc[1], par.sanceng_color):
                click_motion(par.sanceng_click)
                time.sleep(pause_time())
                just_motion(par.rr_loc)

            if not ptg.pixelMatchesColor(par.zhenrongsuo_loc[0], par.zhenrongsuo_loc[1], par.zhenrongsuo_color):
                click_motion(par.zhenrongsuo_loc)
                time.sleep(pause_time())
                just_motion(par.rr_loc)

            click_motion(par.yuling_tiaozhan_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

        time.sleep(pause_time())


def run1():
    # 主循环
    while sett.state:
        # 接受别人邀请的人，只需要点击结算界面
        # 监测胜利还是失败
        sett.yuling_win = ptg.pixelMatchesColor(par.yuling_win_loc[0], par.yuling_win_loc[1], par.yuling_win_color)

        if sett.yuling_win and sett.state:
            # 战斗结束
            # 点击领取奖励
            time.sleep(pause_time())
            click_motion(par.hunshi_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

        time.sleep(pause_time())


def run3():
    # 主循环
    while sett.state:
        # 接受别人邀请的人，只需要点击结算界面
        # 监测胜利还是失败
        sett.yuling_lose = ptg.pixelMatchesColor(par.yuling_lose_loc[0], par.yuling_lose_loc[1], par.yuling_lose_color)

        if sett.yuling_lose and sett.state:
            # 战斗结束
            # 点击领取奖励
            time.sleep(pause_time())
            click_motion(par.hunshi_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

        time.sleep(pause_time())


def run2():
    # 主循环
    while sett.state:
        sett.yuling_jiesuan = ptg.pixelMatchesColor(par.yulingjiesuan_loc[0], par.yulingjiesuan_loc[1], par.yulingjiesuan_color)

        if sett.yuling_jiesuan and sett.state:
            # 领取奖励
            # 点击返回
            sett.yuling_jiesuan = False
            time.sleep(pause_time())
            click_motion(par.yulingjiesuan_loc)
            just_motion(par.rr_loc)
            time.sleep(pause_time()+1)

            # 御灵刷完了
            sett.number += 1
            print('完成第' + str(sett.number) + '次御灵。。。')

        time.sleep(pause_time())


def main():
    gc.enable()
    threads_list = []
    t1 = Thread(target=run1)
    threads_list.append(t1)
    t2 = Thread(target=run2)
    threads_list.append(t2)
    t3 = Thread(target=run_yuling)
    threads_list.append(t3)
    th = Thread(target=ghost1.hook)
    threads_list.append(th)
    t5 = Thread(target=run3)
    threads_list.append(t5)

    for i in threads_list:
        i.start()
    for j in threads_list:
        j.join()


if __name__ == '__main__':
    main()