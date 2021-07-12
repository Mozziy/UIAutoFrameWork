"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: TestGoogleSearch.py
@time: 2021/1/23 17:54
@desc:

"""
from AppFrameWork.PageObject.Google.Google import Google
import pytest

from AppFrameWork.common.Constant import Constants


class TestGoogleSearch:

    test_data = Constants().load_yaml('Google', 'GoogleSearch', Constants.TEST_DATA_DIR)
    def setup_class(self):
        self.main = Google().search_function()

    @pytest.mark.parametrize('value', list(test_data.values()))
    def test_download(self, value):
        """xxxx"""

        # 测试Google主页的搜索功能
        # 进入主页进行搜索.跳转到搜索显示详情页面.跳转雪球主页进行应用下载
        res = self.main.search_function(value).Search_display().download_snow_ball()
        assert 123 == res

    @pytest.mark.parametrize('value', list(test_data.values()))
    def test_cancel(self, value):
        """xxxx"""

        # 测试Google主页的搜索功能
        # 进入主页进行搜索.跳转到搜索显示详情页面.跳转雪球主页进行应用下载
        res = self.main.search_function(value).Search_display().cancel_snow_ball()
        assert 123 == res







