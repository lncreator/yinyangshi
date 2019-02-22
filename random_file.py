#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: random_file.py
@time: 2019/1/8 12:08
@desc: 随机事件
"""

import random


# 生成随机偏移
def bias_random():
    return random.randint(-20, 20)


# 小范围随机偏移
def bias_small():
    return random.randint(-8, 8)


# 获取随机位移
def loc_generate(loc):
    return loc[0] + bias_random(), loc[1] + bias_random()


# 获取小范围随机位移
def loc_small(loc):
    return loc[0] + bias_small(), loc[1] + bias_small()


# 产生时间随机暂停
def pause_time():
    return random.randint(0, 10)/10


# 产生时间随机位移
def bias_time():
    return random.randint(0, 10)/20