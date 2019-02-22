#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: xiezuo_test.py
@time: 2019/1/8 18:58
@desc: 好友协作邀请
"""

import pyautogui as ptg
import yinyangshi.parameters as par
import yinyangshi.setting as sett
from yinyangshi.baigui_test import click_motion, just_motion
from yinyangshi.random_file import *
import time


def run():
    # 刚启动时设置为True
    sett.state = True
    # 主循环
    while sett.state:
        # 监听是否有协作任务
        sett.xiezuo = ptg.pixelMatchesColor(par.xiezuo_loc[0], par.xiezuo_loc[1], par.xiezuo_color)

        while sett.xiezuo:
            # 协作任务出现
            click_motion(par.xiezuo_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

            # 点击完毕
            sett.xiezuo = False


if __name__ == '__main__':
    run()