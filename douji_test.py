#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: douji_test.py
@time: 2019/1/8 12:07
@desc: 斗技测试
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
        # 检查速度慢一些
        time.sleep(pause_time())
        # 斗技开始前，要点击战斗才能开始匹配
        sett.douji_state = ptg.pixelMatchesColor(par.zhan_loc[0], par.zhan_loc[1], par.zhan_color)

        # 高段位的可能会触发banpick界面，需要选择自动上场
        sett.banpick_state = ptg.pixelMatchesColor(par.zidongshang_loc[0], par.zidongshang_loc[1],
                                                   par.zidongshang_color)
        # 进入战斗之后需要点击准备，这里可以更换式神，点击准备的位置跟别的不一样
        sett.waiting_state = ptg.pixelMatchesColor(par.zhunbei_state_loc[0], par.zhunbei_state_loc[1],
                                                   par.zhunbei_state_color)

        # 准备后或者自动上场后，要点击自动，所以这里要检测手动
        sett.shoudong = ptg.pixelMatchesColor(par.shoudong_loc[0], par.shoudong_loc[1], par.shoudong_color)

        # 监测获胜还是失败
        sett.shengli = ptg.pixelMatchesColor(par.shengli_loc[0], par.shengli_loc[1], par.shengli_color)
        sett.shibai = ptg.pixelMatchesColor(par.shibai_loc[0], par.shibai_loc[1], par.shibai_color)

        # 如果无事发生就点一下
        if (sett.douji_state == False) and (sett.banpick_state == False) and (sett.waiting_state == False) and (
                sett.shoudong == False) and (sett.shengli == False) and (sett.shibai == False):
            just_motion(par.rr_loc)
            print(pause_time()+5)
            time.sleep(pause_time()+5)

        if sett.douji_state:
            # 现在是斗技点开界面
            # 点击进入
            click_motion(par.zhan_loc)
            just_motion(par.rr_loc)

            # 进入状态完毕
            sett.douji_state = False

        if sett.banpick_state:
            # 现在是高段位的banpick阶段
            # 点击自动上场
            click_motion(par.zidongshang_loc)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

            # 自动上场完毕
            sett.banpick_state = False

        if sett.waiting_state:
            # 如果没有自动上场界面的话，就是手动准备
            # 点击准备
            click_motion(par.zhunbei_loc)
            just_motion(par.rr_loc)

            # 准备完毕
            sett.waiting_state = False

        if sett.shoudong:
            # 准备之后需要把手动变成自动
            # 点击手动
            click_motion(par.shoudong_click)
            time.sleep(pause_time())
            just_motion(par.rr_loc)

            # 点击完毕
            sett.shoudong = False

        if sett.shengli or sett.shibai:
            # 战斗结束
            # 点击返回
            click_motion(par.shengli_loc)
            sett.number += 1
            just_motion(par.rr_loc)
            print('完成第' + str(sett.number) + '次斗技。。。')

            # 点击完毕
            sett.shengli = False
            sett.shibai = False


if __name__ == '__main__':
    run()
