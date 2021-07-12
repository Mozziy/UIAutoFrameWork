"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: TestDaKa.py
@time: 2021/2/20 下午11:37
@desc:

"""
import pytest
import yaml

from AppFrameWork.PageObject.WeWork.WeWork import WeWork
from AppFrameWork.common.Constant import Constants


class TestDaKa:

    test_data = Constants().load_yaml('WeWork', 'add_number', Constants.TEST_DATA_DIR)
    def setup_class(self):
        self.main = WeWork()

    @pytest.mark.skip()
    def test_daka(self):
        self.main.daka().main_page().work_place()

    @pytest.mark.parametrize('kwargs', [test_data])
    def test_add(self, kwargs):
        self.main.add().main_contact().contact(**kwargs)


