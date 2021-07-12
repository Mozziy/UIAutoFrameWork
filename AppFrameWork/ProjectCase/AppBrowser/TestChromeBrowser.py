"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: TestChromeBrowser.py
@time: 2021/1/28 22:42
@desc:

"""
import pytest

from AppFrameWork.PageObject.DefaultBrowser.DefaultBrowser import DefaultBrowser
from AppFrameWork.common.Constant import Constants


class TestChromeBrowser:

    test_datas = Constants().load_yaml(project_name='DefaultBrowser', path=Constants.TEST_DATA_DIR)
    def setup_class(self):
        self.main = DefaultBrowser()

    def teardown_class(self):
        pass

    @pytest.mark.skip()
    @pytest.mark.parametrize('value', list(test_datas['testChromeBrowser'].values()))
    def testChromeBrowser(self, value):
        self.main.search_function(value)

    @pytest.mark.parametrize('phone,code', [list(test_datas['testxueqiuBrowser'].values())])
    def testsnoallball(self, phone, code):
        self.main.xueqiu_main(phone, code)
