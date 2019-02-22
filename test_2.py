#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: test_2.py
@time: 2018/12/30 18:27
@desc: 骚起来骚起来
"""

import pyautogui as ptg
import yinyangshi.parameters as par
import yinyangshi.setting as sett
import random


# 生成随机偏移
def bias_random():
    return random.randint(-10, 10)


# 获取随机位移
def loc_generate(loc):
    return loc[0] + bias_random(), loc[1] + bias_random()


# 产生时间随机暂停
def pause_time():
    return random.randint(0, 1)


# 产生时间随机位移
def bias_time():
    return random.randint(0, 1)/2


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


# 撒豆
def click_sadou(point):
    location = loc_generate(point)
    ptg.moveTo(location)
    ptg.doubleClick(location)


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
        ptg.PAUSE = 1
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
    aa = [1, 2, 3]
    index = random.sample(aa, 1)[0]
    sadou = None
    if index == 1:
        sadou = par.sadou_loc1
    elif index == 2:
        sadou = par.sadou_loc2
    elif index == 3:
        sadou = par.sadou_loc3

    click_sadou(sadou)


# 开始
def run():
    # 主循环
    while sett.state:

        # 还有可以邀请的好友才能邀请
        while sett.haoyou:
            yaoqinghaoyou()

            # 点击进入
            click_motion(par.jinru_loc)
            jinru = ptg.pixelMatchesColor(par.jinru_loc[0], par.jinru_loc[1], par.jinru_color)
            if jinru:
                # 依然是进入的颜色
                click_motion(par.cancel_loc)
                sett.roll = True
            else:
                sett.haoyou = False

        # 选择鬼王，现在就选择中间这个鬼王
        ptg.PAUSE = 1
        click_motion(par.guiwang2_loc)

        # 点击开始
        ptg.PAUSE = 0.5
        click_motion(par.start_button)
        sett.sadou_state = True
        # 开始后等待2s
        ptg.PAUSE = 5
        ptg.moveTo(par.s1)
        ptg.PAUSE = bias_time()
        ptg.dragRel(50, 0)

        # 开始撒豆
        while sett.sadou_state:

            # 检测是否现在适合撒豆
            fea = ptg.pixelMatchesColor(par.sadou_feature_loc[0], par.sadou_feature_loc[1], par.sadou_feature_color)
            if fea:
                # 依然可以撒豆
                sadou1()
            else:
                # 不可以撒豆了
                sett.sadou_state = False

        # 检测是否是结算界面
        while sett.jiesuan_state:

            # 界面颜色
            jiesuan = ptg.pixelMatchesColor(par.jiesuan_loc[0], par.jiesuan_loc[1], par.jiesuan_color)
            if jiesuan:
                # 是结算页面了
                click_motion(par.jiesuan_loc)
                sett.number += 1
            else:
                # 结算没有完毕
                ptg.PAUSE = 1

        ptg.PAUSE = 3


if __name__ == '__main__':
    run()