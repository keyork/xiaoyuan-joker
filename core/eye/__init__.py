#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  __init__.py
@ Time           :  2024/10/10 14:43:35
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  采集模块
@ History        :  0.1(2024/10/10) - 采集模块(Keyork)
"""
import cv2
import numpy as np
import win32api
import win32con
import win32gui
import win32print
from PIL import ImageGrab

from config import Config


class Eye:
    """眼睛部分

    负责内容：

    1. 获取题目区域
    2. 获取当前题目的图像
    3. 获取下一道题目的图像
    """

    def __init__(self, config: Config) -> None:
        self.window: int = 0
        self.scale: float = 1.0
        self.left: int = 0
        self.top: int = 0
        self.right: int = 0
        self.bottom: int = 0
        self.config = config
        self.img: np.ndarray = None

    def get_screen(self) -> None:
        hdc = win32gui.GetDC(0)
        screen_width = win32print.GetDeviceCaps(hdc, win32con.DESKTOPHORZRES)
        # screen_height = win32print.GetDeviceCaps(hdc, win32con.DESKTOPVERTRES)
        width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        # height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        self.scale = width / screen_width

    def find_window(self) -> None:
        self.window = win32gui.FindWindow(None, self.config.conf.window_name)
        win32gui.SendMessage(
            self.window, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0
        )
        try:
            win32gui.SetForegroundWindow(self.window)
        except:
            pass
        # 获取窗口位置
        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(
            self.window
        )
        self.left = int(self.left / self.scale)
        self.top = int(self.top / self.scale)
        self.right = int(self.right / self.scale)
        self.bottom = int(self.bottom / self.scale)

    def get_curr_question(self) -> None:
        """获取当前题目的图像"""
        window_height = self.bottom - self.top
        window_width = self.right - self.left

        self.img = ImageGrab.grab(
            (
                self.left + window_width * self.config.conf.eye.left,
                self.top + window_height * self.config.conf.eye.top,
                self.right - window_width * self.config.conf.eye.right,
                self.bottom - window_height * self.config.conf.eye.bottom,
            )
        )
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2GRAY)
        # 缩放成原来的1/2
        self.img = cv2.resize(
            self.img,
            (self.img.shape[1] // 2, self.img.shape[0] // 2),
            interpolation=cv2.INTER_AREA,
        )
