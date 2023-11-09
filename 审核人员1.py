import pyautogui
import time
import json

time.sleep(2)
# 从JSON文件读取操作序列
with open('point/point.json', 'r') as file:
    actions = json.load(file)

# 循环10次
for _ in range(18):
    for action in actions:
        # 移动到指定位置并点击
        pyautogui.moveTo(*action["location"])
        pyautogui.click()
        time.sleep(action["wait_time"])
