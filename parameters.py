#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: parameters.py
@time: 2018/12/30 16:55
@desc: 放参数的文件
"""

"""一些基础数据"""
# 窗口位置
left_top = (393, 221)
left_bottom = (392, 855)
right_top = (1523, 222)
right_bottom = (1524, 858)

# 窗口大小
width = 1130
height = 633
# 图片文件位置
path = 'C:/Users/Administrator/Desktop/Python3Space/yinyangshi/image/'

"""tk面板设置"""
# 窗口位置和大小
left_up_loc = "300x100+1550+190"

"""好友协作任务邀请"""
xiezuo_loc = (1163, 581)
xiezuo_color = (86, 179, 97)

"""百鬼夜行"""
# 百鬼夜行图标
baigui_pic = path + '百鬼夜行.png'
# 进入图标
jinru_pic = path + '进入.png'
jinru_loc = (1222, 684)
jinru_color = (243, 178, 94)
# 邀请好友
yaoqing_pic = path + '邀请好友.png'
yaoqing_loc = (660, 683)
yaoqing_color = (245, 238, 229)
# 邀请好友后 点击位置1
yaoqing1_loc = (911, 433)
yaoqing1_color = (234, 199, 160)
# 邀请好友后 点击位置2
yaoqing2_loc = (1159, 437)
yaoqing2_color = (243, 199, 160)

# 邀请好友界面滚动距离
roll_distance = -150
# 邀请好友界面空白点击位置
blank_click = (1137, 364)
blank_color = (167, 144, 122)
# 邀请好友退出界面位置
quit_click = (1381, 513)

# 好友点击位置
haoyou_click = (744, 335)
# 跨区点击位置
kuaqi_click = (879, 334)

# 好友取消位置
cancel_loc = 697, 650

# 百鬼夜行选鬼王界面
guiwang1_loc = (500, 621)
guiwang2_loc = (951, 625)
guiwang3_loc = (1400, 612)
# 进入界面后不变的颜色点
choose_loc = (1427, 304)
choose_color = (142, 126, 114)

# 点击开始
start_button = (1446, 796)

# 改变豆子个数
s1 = (733, 830)
s2 = (1000, 830)

# 冰冻数据
ice_loc = (429, 295)
ice_color = (193, 193, 229)

# 撒豆方式1的位置点
sadou_loc1 = (1400, 650)
sadou_loc2 = (959, 650)
sadou_loc3 = (460, 650)
sadou_loc4 = (1180, 650)
sadou_loc5 = (710, 650)

# 撒豆特征点
sadou_feature_loc = (963, 292)
sadou_feature_color = (49, 34, 32)

# 结算界面
jiesuan_loc = (563, 242)
jiesuan_color = (131, 62, 161)

# 点击离开结算
exit_loc = (1510, 493)
exit_color = (15, 21, 52)

"""魂十"""
# 接受别人邀请
hs_yaoqing_loc = (502, 438)
hs_yaoqing_color = (87, 179, 98)

# 自动接收
hunshi_yaoqing_loc = (596, 431)
hunshi_yaoqing_color = (186, 144, 90)

# 魂十胜利界面
hunshi_loc = (913, 241)
hunshi_color = (161, 136, 87)

# 魂十结算界面
hs_jiesuan_loc = (751, 829)
hs_jiesuan_color = (37, 35, 19)

"""斗技"""
# 随机一个位置，只移动不点击
rr_loc = (950, 515)

# 点击“战”开始斗技
zhan_loc = (1378, 720)
zhan_color = (188, 139, 75)

# banpick界面（不一定会有）（也有自动和手动）
zidongshang_loc = (450, 322)
zidongshang_color = (253, 252, 252)

# 打架前要点准备
zhunbei_state_loc = (1435, 827)
zhunbei_state_color = (220, 180, 121)
zhunbei_loc = (1435, 750)

# 手动
shoudong_click = (424, 812)
shoudong_loc = (823, 849)
shoudong_color = (21, 78, 159)

# 胜利，点一下就退出啦
shengli_loc = (815, 285)
shengli_color = (119, 23, 15)
# 失败，点一下就退出啦
shibai_loc = (801, 271)
shibai_color = (78, 70, 87)

"""御灵"""
# 点击挑战的界面状态
yuling_tiaozhan_loc = (1276, 665)
yuling_tiaozhan_color = (243, 178, 94)

# 三层的边框颜色
sanceng_loc = (885, 457)
sanceng_color = (125, 22, 236)
sanceng_click = (836, 490)

# 阵容锁
zhenrongsuo_loc = (1044, 586)
zhenrongsuo_color = (157, 150, 208)

# 黑豹位置和颜色
heibao_loc = (1048, 770)
heibao_color = (252, 196, 142)

# 战斗的状态
yuling_loc = (894, 846)
yuling_color = (45, 28, 27)

# 御灵获胜
yuling_win_loc = (817, 339)
yuling_win_color = (131, 27, 18)

# 御灵失败
yuling_lose_loc = (800, 335)
yuling_lose_color = (78, 70, 87)

# 御灵结算
yulingjiesuan_loc = (1059, 687)
yulingjiesuan_color = (211, 147, 25)

"""业原火"""


"""魂十（邀请别人）"""
zudui = (615, 794)
yuhun = (614, 677)

shiceng_move = (830, 530)
shiceng = (820, 708)

# 创建队伍
create_hunshi = (1324, 783)
private_loc = (1074, 670)
create_click = (1173, 748)

# 选择十层滚动距离
roll_distance2 = -800

# 创建队伍完成后，开启双倍，和邀请队友
invite_duiyou = (1029, 640)
duiyou = (828, 409)
yaoqing_click = (1079, 731)

# 开启双倍
shuangbei1 = (1456, 258)
shuangbei2 = (1124, 411)
shuangbei3 = (1444, 483)

# 等队友进来之后，开始状态变色后开始
kaishi_loc = (1323, 756)
kaishi_color = (243, 178, 94)


"""为崽而战"""
ffb_start_loc = (1460, 769)
ffb_start_color = (45, 41, 36)

ffb_win_loc = (1252, 815)
ffb_win_color = (136, 102, 84)

ffb_lose = (1210, 584)
ffb_lose_color = (255, 255, 255)