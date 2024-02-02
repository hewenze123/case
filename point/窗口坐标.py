import pyautogui
import tkinter as tk

# 创建一个窗口
root = tk.Tk()
root.geometry("300x100")

# 创建一个标签用于显示坐标
label = tk.Label(root, text="")
label.pack()


# 更新鼠标坐标的函数
def update_coordinates():
    x, y = pyautogui.position()
    label.config(text=f"鼠标坐标：X={x}, Y={y}")
    root.after(100, update_coordinates)


# 启动更新坐标的函数
update_coordinates()

root.mainloop()
