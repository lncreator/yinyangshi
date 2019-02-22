#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: test_1.py
@time: 2018/12/30 16:48
@desc: pyautogui测试1
"""

import pyautogui as ptg
import yinyangshi.parameters as par

# print(ptg.position())
# x, y = ptg.position()
# ptg.click(x, y, button='left')

# pic_baigui = ptg.screenshot(par.baigui, region=(par.left_top[0], par.left_top[1], par.width, par.height))

a = ptg.locateCenterOnScreen(par.yaoqing, grayscale=False)
print(a)
ptg.click(a)