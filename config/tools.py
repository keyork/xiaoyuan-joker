#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  tools.py
@ Time           :  2024/10/10 16:58:16
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  None
@ History        :  0.1(2024/10/10) - None(Keyork)
"""

import json
from typing import Dict

import yaml


def load_config(path: str) -> Dict:
    """加载配置

    Args:
        path (str): 配置文件路径

    Returns:
        Dict: 配置信息
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.SafeLoader)


def load_json_config(path: str) -> Dict:
    """加载配置

    Args:
        path (str): 配置文件路径

    Returns:
        Dict: 配置信息
    """
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config


class DictToClass:

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToClass(value))
            else:
                setattr(self, key, value)
