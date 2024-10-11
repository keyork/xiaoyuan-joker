#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  main.py
@ Time           :  2024/10/10 14:42:56
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  入口
@ History        :  0.1(2024/10/10) - 入口(Keyork)
"""
import argparse
import time
from config import Config
from core.eye import Eye
from core.brian import Brain
from core.hand import Hand
import cv2

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", type=str, default="etc/config.yaml")
    args.add_argument("--type", "-t", type=str, default="比大小")
    args = args.parse_args()
    config = Config(args)
    eye = Eye(config)
    brain = Brain(config)
    hand = Hand(config)
    curr_answer = None
    eye.get_screen()
    eye.find_window()
    while True:
        start = time.time()
        eye.get_curr_question()
        brain.get_img(eye.img)
        brain.get_question()
        brain.compute()
        # 打印所有内容, 包含换行符
        print(brain.question_str, brain.answer)
        # time.sleep(0.05)
        # 保存图像
        # cv2.imwrite("question.png", brain.img)
        # 和上一个answer一样才写
        if curr_answer != brain.answer:
            curr_answer = brain.answer
            continue
        else:
            if curr_answer is None:
                continue
            # 开始写字
            x = eye.left + (eye.right - eye.left) // 10
            y = (eye.top + eye.bottom) // 2
            hand.moveto(x, y)
            hand.get_answer(curr_answer)
            hand.write()
            time.sleep(0.3)
