#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  gcd.py
@ Time           :  2024/10/10 21:50:13
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  None
@ History        :  0.1(2024/10/10) - None(Keyork)
"""


def get_gcd(question: str) -> int:
    """获取最大公因数

    Args:
        question (str): 问题，形如(16,12)=?

    Returns:
        int: 答案
    """
    # 从问题中提取数字
    try:
        if question[-1] == "?":
            num1, num2 = map(int, question[1:-3].split(","))
        else:
            num1, num2 = map(int, question[1:-2].split(","))
        print(num1, num2)
    except:
        return None
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return str(num1)
