"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: DecorateComponent.py
@time: 2021/1/16 18:07
@desc: 装饰器

"""


def black(fun):
    def run(*args, **kwargs):
        try:
            fun()
        except:
            return

    return run









