#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  action.py
@ Time           :  2024/10/10 22:02:19
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  None
@ History        :  0.1(2024/10/10) - None(Keyork)
"""
import time
import pyautogui

# 设置鼠标速度为非常快
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01


class Action:

    def __init__(self) -> None:
        self.action = None
        self.init_x = 0
        self.init_y = 0
        self.char_idx = 0

    def draw_method(self, char: str) -> None:
        if char == "1":
            # 绘制1
            self.action = [
                "d",
                "2 10",
                "u",
            ]
        elif char == "2":
            self.action = [
                "d",
                "5 0",
                "0 5",
                "-5 5",
                "5 0",
                "u",
            ]
        elif char == "3":
            self.action = [
                "d",
                "5 0",
                "-5 5",
                "5 0",
                "0 5",
                "-5 0",
                "u",
            ]
        elif char == "4":
            self.action = [
                "d",
                "0 5",
                "5 0",
                "0 -5",
                "0 15",
                "u",
            ]
        elif char == "5":
            self.action = [
                "5 0",
                "d",
                "-5 0",
                "0 5",
                "5 0",
                "0 5",
                "-5 0",
                "u",
            ]
        elif char == "6":
            self.action = [
                "5 0",
                "d",
                "-5 10",
                "5 0",
                "0 -5",
                "-9 0",
                "u",
            ]
        elif char == "7":
            self.action = [
                "d",
                "5 0",
                "-5 15",
                "u",
            ]
        elif char == "8":
            self.action = [
                "5 5",
                "d",
                "-5 -5",
                "10 0",
                "-10 10",
                "10 0",
                "-5 -5",
                "u",
            ]
        elif char == "9":
            self.action = [
                "5 0",
                "d",
                "-5 0",
                "0 -5",
                "5 0",
                "0 10",
                "-5 0",
                "u",
            ]
        elif char == "0":
            self.action = [
                "d",
                "5 0",
                "0 10",
                "-5 0",
                "0 -10",
                "u",
            ]
        elif char == "<":
            self.action = [
                "d",
                "-5 5",
                "0 10",
                "u",
            ]
        elif char == ">":
            self.action = [
                "d",
                "5 5",
                "0 10",
                "u",
            ]
        elif char == "=":
            self.action = [
                "d",
                "5 0",
                "u",
                "0 5",
                "d",
                "5 5",
                "u",
            ]
        elif char == ".":
            self.action = [
                "5 10",
                "d",
                "0 1",
                "u",
            ]

    def action_map(self, action: str) -> None:
        if len(action) == 1:
            if action == "u":
                pyautogui.mouseUp()
            elif action == "d":
                pyautogui.mouseDown()
        else:
            x, y = map(int, action.split())
            pyautogui.move(x * 9, y * 9)
        time.sleep(0.01)

    def go_right(self) -> None:
        self.char_idx += 1
        pyautogui.moveTo(self.init_x + self.char_idx * 100, self.init_y)
        time.sleep(0.01)

    def moveto(self, x, y):
        pyautogui.moveTo(x, y)
        self.init_x = x
        self.init_y = y
        self.char_idx = 0
