import ctypes
import time
import threading
import tkinter as tk
from tkinter import messagebox

# 定义一个函数来调整屏幕亮度
def adjust_brightness():
    # 调用Windows API来设置屏幕亮度
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)  # 防止屏幕锁定
    ctypes.windll.user32.SendMessageW(-1, 0x0112, 0xF170, 0)  # 设置屏幕亮度为0

# 定义一个函数来弹出倒计时提示框
def show_message_box():
    root = tk.Tk()
    root.withdraw()  # 隐藏根窗口

    # 弹出倒计时提示框
    messagebox.showinfo("倒计时结束", "时间到了！")

# 在一个线程中执行调整屏幕亮度和弹出提示框
def after_timer_actions():
    adjust_brightness()
    show_message_box()

# 使用线程来执行时间结束后的操作
def perform_actions_after_timer():
    t = threading.Thread(target=after_timer_actions)
    t.start()

# 如果这个文件作为独立运行的脚本，执行倒计时
if __name__ == "__main__":
    # 模拟一个5秒钟的倒计时
    time.sleep(5)
    perform_actions_after_timer()
