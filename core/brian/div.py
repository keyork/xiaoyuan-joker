#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  div.py
@ Time           :  2024/10/11 10:56:57
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  除法
@ History        :  0.1(2024/10/11) - 除法(Keyork)
"""


def get_div(question: str) -> int:
    """获取除法结果

    Args:
        question (str): 问题，形如(16,12)=?

    Returns:
        int: 答案
    """
    # 从问题中提取数字
    try:
        question.replace("+", "?")
        question = question.split("=")[0]
        if "?" in question:
            num1, num2 = map(float, question.split("?"))
        else:
            num1, num2 = map(float, question.split("÷"))
        print(num1, num2)
    except:
        return None
    result = num1 / num2
    # 处理精度问题
    # 只留存小数点后两位
    result = round(result, 2)
    # 如果是整数，返回整数
    if result.is_integer():
        return str(int(result))
    return str(result)
