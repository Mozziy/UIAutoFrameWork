"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: conftest.py
@time: 2020/12/26 21:41
@desc: fixture为session级别是可以跨.py模块调用的

"""

import pytest



@pytest.fixture(scope='session')
def sessionfix():
    return "fixture"


