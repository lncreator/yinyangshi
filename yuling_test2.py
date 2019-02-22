#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: yuling_test2.py
@time: 2019/1/17 13:11
@desc: 御灵测试2：看看是否能解决内存溢出的问题
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


def run3():
    # 监测胜利还是失败
    sett.yuling_win = ptg.pixelMatchesColor(par.yuling_win_loc[0], par.yuling_win_loc[1], par.yuling_win_color)
    sett.yuling_lose = ptg.pixelMatchesColor(par.yuling_lose_loc[0], par.yuling_lose_loc[1], par.yuling_lose_color)

    if sett.yuling_lose or sett.yuling_win:
        # 战斗结束
        # 点击领取奖励
        click_motion(par.hunshi_loc)
        time.sleep(pause_time())
        click_motion(par.hs_jiesuan_loc)

        time.sleep(pause_time() + 1)


def run2():
    sett.yuling_jiesuan = ptg.pixelMatchesColor(par.yulingjiesuan_loc[0], par.yulingjiesuan_loc[1], par.yulingjiesuan_color)

    if sett.yuling_jiesuan and sett.state:
        # 领取奖励
        # 点击返回
        time.sleep(pause_time() + 2)
        sett.number += 1
        click_motion(par.hs_jiesuan_loc)
        time.sleep(pause_time())
        click_motion(par.hs_jiesuan_loc)
        time.sleep(pause_time())
        click_motion(par.hs_jiesuan_loc)

        time.sleep(pause_time() + 1)

        # 御灵刷完了
        print('完成第' + str(sett.number) + '次御灵。。。')


def main():
    while sett.state:
        run_yuling()
        run2()
        run3()
        time.sleep(pause_time())


if __name__ == '__main__':
    main()