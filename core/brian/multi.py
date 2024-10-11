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
        question = question.split("=")[0]
        num1, num2 = map(float, question.split("x"))
        print(num1, num2)
    except:
        return None
    result = num1 * num2
    # 处理精度问题
    # 只留存小数点后两位
    result = round(result, 5)
    # 如果是整数，返回整数
    if result.is_integer():
        return str(int(result))
    return str(result)
