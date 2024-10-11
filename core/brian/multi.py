#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  multi.py
@ Time           :  2024/10/11 10:42:17
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  乘法
@ History        :  0.1(2024/10/11) - 乘法(Keyork)
"""


def get_multi(question: str) -> int:
    """获取乘法结果

    Args:
        question (str): 问题，形如(16,12)=?

    Returns:
        int: 答案
    """
    # 从问题中提取数字
    try:
        if question[-1] == "?":
            num1, num2 = map(int, question[0:-2].split("x"))
        else:
            num1, num2 = map(int, question[0:-1].split("x"))
        print(num1, num2)
    except:
        return None
    return str(num1 * num2)
