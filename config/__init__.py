#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  __init__.py
@ Time           :  2024/10/10 16:58:08
@ Author         :  Keyork
@ Version        :  0.1
@ Description    :  None
@ History        :  0.1(2024/10/10) - None(Keyork)
"""
import os
from typing import Dict


from .tools import DictToClass, load_config


class BaseConfig:

    def __init__(self, config: Dict) -> None:
        self.config = DictToClass(config)


class Config:

    def __init__(self, args) -> None:

        self.args_conf = BaseConfig(vars(args)).config
        self.conf = BaseConfig(load_config(self.args_conf.config)).config
