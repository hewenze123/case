from pynput.mouse import Listener


def on_move(x, y):
    print(f"鼠标坐标：({x}, {y})")


# 创建监听器
with Listener(on_move=on_move) as listener:
    listener.join()