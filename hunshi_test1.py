#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: hunshi_test1.py
@time: 2018/12/31 18:51
@desc: 魂十测试1
"""

import pyautogui as ptg
import time
import yinyangshi.parameters as par
import yinyangshi.setting as sett
from yinyangshi.baigui_test import click_motion, just_motion
from yinyangshi.random_file import *


def run():
    # 刚启动时设置为True
    sett.state = True
    # 主循环
    while sett.state:
        # 接受别人邀请的人，只需要点击结算界面
        # 监测胜利还是失败
        sett.hunshi_win = ptg.pixelMatchesColor(par.hunshi_loc[0], par.hunshi_loc[1], par.hunshi_color)
        sett.hs_jiesuan = ptg.pixelMatchesColor(par.hs_jiesuan_loc[0], par.hs_jiesuan_loc[1], par.hs_jiesuan_color)

        if sett.hunshi_win and sett.state:
            # 战斗结束
            # 点击领取奖励
            time.sleep(pause_time())
            click_motion(par.hunshi_loc)
            time.sleep(pause_time()+2)
            just_motion(par.rr_loc)

            # 点击完毕
            sett.hunshi_win = False

        if sett.hs_jiesuan and sett.state:
            # 领取奖励
            # 点击返回
            sett.hs_jiesuan = False
            time.sleep(pause_time()+2)
            click_motion(par.hs_jiesuan_loc)
            just_motion(par.rr_loc)
            time.sleep(pause_time()+2)

            # 魂十刷完了
            sett.number += 1
            print('完成第' + str(sett.number) + '次魂十。。。')


if __name__ == '__main__':
    run()