"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: StockSearch.py
@time: 2021/1/24 20:18
@desc:

"""
import pytest

from AppFrameWork.PageObject.XueQiu.XueQiu import XueQiu
from AppFrameWork.common.Constant import Constants
import hamcrest

class TestStockSearch:

    test_data = Constants().load_yaml('XueQiu', 'StockSearch', Constants.TEST_DATA_DIR)
    def setup_class(self):
        self.main = XueQiu().search_function()

    # @pytest.mark.parametrize('value', list(test_data.values()))
    # def test_stock_search(self, value):
    #
    #     curren_price = self.main.mainpage_search_function(value).get_stock_price()
    #     hamcrest.assert_that(float(curren_price), hamcrest.close_to(250, 268))

    # @pytest.mark.parametrize('phone, code', [[166666666666, 2367]])
    def test_webview(self, phone=16666666666, code=898226):
        """测试webview"""
        self.main.click_trade().register_account(phone, code)



