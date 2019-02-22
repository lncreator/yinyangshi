#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: hunshi_yaoqing1.py
@time: 2019/1/16 19:32
@desc: 魂十作为邀请的人的脚本
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


def qidong():
    # 最开始点击开始魂十等邀请界面
    click_small(par.zudui)
    time.sleep(pause_time())
    click_small(par.yuhun)
    time.sleep(pause_time()+1)
    just_motion(par.shiceng_move)
    time.sleep(pause_time())
    ptg.scroll(par.roll_distance2)
    time.sleep(pause_time())
    click_small(par.shiceng)

    # 创建队伍
    time.sleep(pause_time())
    click_small(par.create_hunshi)
    time.sleep(pause_time())
    click_small(par.private_loc)
    time.sleep(pause_time())
    click_small(par.create_click)

    # 邀请好友
    time.sleep(pause_time())
    click_small(par.invite_duiyou)
    time.sleep(pause_time())
    click_small(par.duiyou)
    time.sleep(pause_time())
    click_small(par.yaoqing_click)
    time.sleep(pause_time())


# 开启双倍
def shuangbei():
    click_small(par.shuangbei1)
    time.sleep(pause_time())
    click_small(par.shuangbei2)
    time.sleep(pause_time())
    click_small(par.shuangbei3)
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
            click_motion(par.hs_jiesuan_loc)
            click_motion(par.hs_jiesuan_loc)

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
            click_motion(par.hs_jiesuan_loc)
            time.sleep(pause_time())
            click_motion(par.hs_jiesuan_loc)
            time.sleep(pause_time())
            click_motion(par.hs_jiesuan_loc)

            time.sleep(pause_time()+3)

            # 魂十刷完了
            print('完成第' + str(sett.number) + '次魂十。。。')

        time.sleep(pause_time())


def run3():
    """检测组队，是否队友就位"""
    while sett.state:
        sett.duiyou = ptg.pixelMatchesColor(par.kaishi_loc[0], par.kaishi_loc[1], par.kaishi_color)

        if sett.duiyou and sett.state:
            # 领取奖励
            # 点击返回
            time.sleep(pause_time())
            click_small(par.kaishi_loc)

            time.sleep(pause_time()+3)
        time.sleep(pause_time())


def main():
    qidong()

    threads_list = []
    t1 = Thread(target=run1)
    threads_list.append(t1)
    t2 = Thread(target=run2)
    threads_list.append(t2)
    th = Thread(target=ghost1.hook)
    threads_list.append(th)
    t3 = Thread(target=run3)
    threads_list.append(t3)
    for i in threads_list:
        i.start()
    for j in threads_list:
        j.join()


if __name__ == '__main__':
    main()