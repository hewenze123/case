import case
import time
import os


time.sleep(2)
image_path = "图片/审核成功.png"
# 定义操作序列
actions = [
    {"location": (475, 315), "wait_time": 1},  # 全选
    {"location": (1169, 246), "wait_time": 1},  # 审核
    {"location": (767, 575), "wait_time": 60},  # 确认
    {"location": (815, 575), "wait_time": 1}  # 确认
]


# 循环10次
for _ in range(10):
    for action in actions:
        # 移动到指定位置并点击
        case.moveTo(*action["location"])
        case.click()
        time.sleep(action["wait_time"])

