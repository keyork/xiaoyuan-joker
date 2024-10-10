#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  __init__.py
@ Time           :  2024/10/10 14:43:45
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  写字模块
@ History        :  0.1(2024/10/10) - 写字模块(Keyork)
"""
from config import Config
from .action import Action


class Hand:
    """手部分

    负责内容：

    1. 将计算结果转换成笔迹
    2. 执行笔迹
    """

    def __init__(self, config: Config) -> None:
        self.config: Config = config
        self.answer: str = None
        self.action: Action = Action()

    def get_answer(self, answer: str) -> None:
        self.answer = answer

    def write(self) -> None:
        for idx in range(len(self.answer)):
            self.action.draw_method(self.answer[idx])
            for act in self.action.action:
                self.action.action_map(act)
            self.action.go_right()

    def moveto(self, x: int, y: int) -> None:
        self.action.moveto(x, y)
