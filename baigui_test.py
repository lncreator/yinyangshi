#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: baigui_test.py
@time: 2018/12/31 15:08
@desc:版本3：通过一直检测状态观察是什么状态采取什么情况
"""


import pyautogui as ptg
import yinyangshi.parameters as par
import yinyangshi.setting as sett
import sys
import os
import pythoncom
import pyHook
import gc
import time
from sys import getrefcount

from yinyangshi.random_file import *


# 邀请好友点击
def invite():
    location = loc_generate(par.yaoqing_loc)
    ptg.moveTo(location, duration=bias_time())
    ptg.click(location)


# 选择好友1并点击
def haoyou1():
    location = loc_generate(par.yaoqing1_loc)
    ptg.moveTo(location, duration=bias_time())
    ptg.click(location)


# 选择好友2并点击
def haoyou2():
    location = loc_generate(par.yaoqing2_loc)
    ptg.moveTo(location, duration=bias_time())
    ptg.click(location)


# 普通移动点击操作
def click_motion(point):
    location = loc_generate(point)
    ptg.moveTo(location, duration=bias_time()/3)
    ptg.click(location)


# 移动一点的点击
def click_small(point):
    location = loc_small(point)
    ptg.moveTo(location, duration=bias_time()/3)
    ptg.click(location)


# 普通移动操作
def just_motion(point):
    location = loc_generate(point)
    ptg.moveTo(location, duration=bias_time()/3)


# 撒豆
def click_sadou(point):
    location = loc_generate(point)
    ptg.moveTo(location, duration=bias_time()/2)
    ptg.click(location)
    ptg.PAUSE = pause_time() / 5
    ptg.click(location)


# 滚动好友列表
def roll_motion():
    ptg.click(par.blank_click)
    ptg.moveTo(par.yaoqing1_loc)
    ptg.scroll(par.roll_distance)


# 邀请好友总操作
def yaoqinghaoyou():
    # 邀请好友点击
    invite()

    # 是否有滚动的需要
    if sett.roll:
        roll_motion()
        ptg.PAUSE = 0.5 + pause_time()/2
        sett.roll = False

    # 选择好友1
    haoyou1()
    color_after = ptg.pixelMatchesColor(par.blank_click[0], par.blank_click[1], par.blank_color)
    if color_after:
        # 颜色相同，不能邀请，界面未变，尝试邀请第二个好友
        haoyou2()
        color_after = ptg.pixelMatchesColor(par.blank_click[0], par.blank_click[1], par.blank_color)
        if color_after:
            # 颜色相同，好友2不能邀请，需要滚动
            sett.roll = True
            # 退出好友邀请界面
            click_motion(par.quit_click)
        else:
            # 邀请好友完毕
            sett.invite = True

    else:
        # 邀请好友完毕
        sett.invite = True

    # 退出好友邀请界面
    click_motion(par.quit_click)


# 撒豆方式1
def sadou1():
    # aa = [1, 2, 3, 4, 5, 1, 1]
    # index = random.sample(aa, 1)[0]

    index = int(sett.count % 5 + 1)
    sett.count += 1

    sadou = None
    if index == 1:
        sadou = par.sadou_loc1
    elif index == 2:
        sadou = par.sadou_loc2
    elif index == 3:
        sadou = par.sadou_loc3
    elif index == 4:
        sadou = par.sadou_loc4
    elif index == 5:
        sadou = par.sadou_loc5

    click_sadou(sadou)
    time.sleep(pause_time()/4)


# 选择鬼王
def guiwang_choose():
    ptg.PAUSE = 0.5 + pause_time()/2
    click_motion(par.guiwang2_loc)

    # 点击开始
    click_motion(par.start_button)
    sett.sadou_state = True
    # 开始后等待6s
    ptg.PAUSE = 6 + pause_time()/2
    ptg.moveTo(par.s1)
    ptg.PAUSE = pause_time()/2
    ptg.dragRel(100, 0)


def onKeyboardEvent(event):
    key = event.Key
    if key == 'S' or key == 'Oem_3':
        print('脚本已停止。。。')
        sett.state = False
    if key == 'Q' or key == 'Escape':
        print('脚本已退出。。。')
        os._exit(0)
    # if key == '1':
    #     print('运行【百鬼夜行】')
    #     run()
    return True


def hook():
    pythoncom.CoInitialize()
    # 创建一个钩子管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘钩子qq
    hm.HookKeyboard()
    # 进入循环，如果不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()
    pythoncom.CoUninitialize()


# 开始
def run():
    # 主循环
    while sett.state:
        sett.jinru_state = ptg.pixelMatchesColor(par.jinru_loc[0], par.jinru_loc[1], par.jinru_color)
        sett.guiwang_state = ptg.pixelMatchesColor(par.choose_loc[0], par.choose_loc[1], par.choose_color)
        sett.jiesuan_state = ptg.pixelMatchesColor(par.jiesuan_loc[0], par.jiesuan_loc[1], par.jiesuan_color)

        while sett.jinru_state and sett.state:
            # 现在是进入页面
            # 点击进入
            click_motion(par.jinru_loc)

            # 进入状态完毕
            sett.jinru_state = False

        while sett.guiwang_state and sett.state:
            # 现在是选择鬼王的页面
            # 点击选择鬼王，暂时只能选择中间的鬼王
            guiwang_choose()

            # 选择完毕
            sett.guiwang_state = False

        while sett.sadou_state and sett.state:
            # 现在是撒豆的页面
            # 开始撒豆

            # 需要时刻检测是否现在适合撒豆
            sett.sadou_state = ptg.pixelMatchesColor(par.sadou_feature_loc[0], par.sadou_feature_loc[1], par.sadou_feature_color)
            '''
            ice = ptg.pixelMatchesColor(par.ice_loc[0], par.ice_loc[1], par.ice_color)
            # 如果有冰冻效果，则暂停撒豆
            if ice:
                sett.state = False
            else:
                sett.state = True
            '''
            # 没问题的话可以撒豆
            sadou1()

        while sett.jiesuan_state and sett.state:
            # 现在是结算的页面
            # 关闭结算页面，记录一次撒豆次数
            click_motion(par.jiesuan_loc)
            sett.number += 1
            print('完成第' + str(sett.number) + '次百鬼夜行。。。')

            # 结算完毕，暂停3s
            sett.jiesuan_state = False
            ptg.PAUSE = pause_time()/2 + 2

        # print(getrefcount(sett.jiesuan_state))


if __name__ == '__main__':
    run()