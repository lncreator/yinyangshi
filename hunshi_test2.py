#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: hunshi_test2.py
@time: 2018/12/31 18:51
@desc: 魂十测试1
"""

import pyautogui as ptg
import gc
import sys
import line_profiler
import weakref
import time
import yinyangshi.parameters as par
import yinyangshi.setting as sett
from yinyangshi.baigui_test import click_motion, just_motion
from yinyangshi.random_file import *


class Par(object):
    def __init__(self):
        # 随机一个位置，只移动不点击
        self.rr_loc = (950, 515)

        # 魂十胜利界面
        self.hunshi_loc = (913, 241)
        self.hunshi_color = (161, 136, 87)

        # 魂十结算界面
        self.hs_jiesuan_loc = (751, 829)
        self.hs_jiesuan_color = (37, 35, 19)


a = Par()


def run():

    # 接受别人邀请的人，只需要点击结算界面
    # 监测胜利还是失败

    r = weakref.ref(a)

    hunshi_win = ptg.pixelMatchesColor(r().hunshi_loc[0], r().hunshi_loc[1], r().hunshi_color)
    hs_jiesuan = ptg.pixelMatchesColor(r().hs_jiesuan_loc[0], r().hs_jiesuan_loc[1], r().hs_jiesuan_color)

    if hunshi_win:
        # 战斗结束
        # 点击领取奖励
        time.sleep(pause_time())
        click_motion(r().hunshi_loc)
        time.sleep(pause_time()+2)
        just_motion(r().rr_loc)

        # 点击完毕
        # hunshi_win = False

    if hs_jiesuan:
        # 领取奖励
        # 点击返回
        # hs_jiesuan = False
        time.sleep(pause_time()+2)
        click_motion(r().hs_jiesuan_loc)
        just_motion(r().rr_loc)
        time.sleep(pause_time()+2)

        # 魂十刷完了
        sett.number += 1
        print('完成第' + str(sett.number) + '次魂十。。。')

    del r
    for i in locals().keys():
        del locals()[i]
    for j, k in globals().items():
        del globals()[j]
    gc.collect()


if __name__ == '__main__':
    # 刚启动时设置为True
    # sett.state = True
    # 主循环
    # pro = line_profiler.LineProfiler(run)
    # pro.enable()
    # times = 5
    while True:
        # times = times - 1
        run()
        for j, k in globals().items():
            del globals()[j]
        gc.collect()
    # pro.disable()
    # pro.print_stats(sys.stdout)