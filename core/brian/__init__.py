#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  __init__.py
@ Time           :  2024/10/10 14:43:20
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  计算模块
@ History        :  0.1(2024/10/10) - 计算模块(Keyork)
"""

import cv2
import numpy as np
import pytesseract
import easyocr

from config import Config
from .gcd import get_gcd
from .lcm import get_lcm
from .multi import get_multi
from .div import get_div

pytesseract.pytesseract.tesseract_cmd = "D:/install/ocr/tesseract.exe"


class Brain:
    """大脑部分

    负责内容：

    1. 将图像的内容转换成算式
    2. 计算结果
    3. 保存结果列表
    """

    def __init__(self, config: Config) -> None:
        self.config: Config = config
        self.img: np.ndarray = None
        self.question_str: str = None
        self.answer: str = None
        self.reader = easyocr.Reader(["ch_sim", "en"])

    def get_img(self, img: np.ndarray) -> None:
        self.img = img
        _, self.img = cv2.threshold(self.img, 150, 255, cv2.THRESH_BINARY)

    def get_question(self) -> None:
        # self.question_str = pytesseract.image_to_string(
        #     self.img,
        #     lang=self.config.conf.brain.lang,
        #     config=self.config.conf.brain.ocr_config,
        # )
        # self.question_str = self.question_str.split("\n")[0]
        self.question_str = self.reader.readtext(
            self.img,
            decoder="beamsearch",
            beamWidth=50,
            batch_size=4,
            allowlist="?=÷+-x.%0123456789(),[]",
            paragraph=True,
            detail=0,
        )
        # 这是个list, 合并成一个str
        self.question_str = "".join(self.question_str)

    def compute(self) -> None:
        if self.config.args_conf.type == "gcd":
            self.answer = get_gcd(self.question_str)
        if self.config.args_conf.type == "lcm":
            self.answer = get_lcm(self.question_str)
        if self.config.args_conf.type == "multi":
            self.answer = get_multi(self.question_str)
        if self.config.args_conf.type == "div":
            self.answer = get_div(self.question_str)
