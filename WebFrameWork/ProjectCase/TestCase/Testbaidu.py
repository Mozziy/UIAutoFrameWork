"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Testbaidu
@time: 2020/12/30 23:50
@desc:
"""

import pytest, os, allure
from WebFrameWork.BasePage.Constant import Constants
from WebFrameWork.PageObject.BaiduMainPage.MainPage import MainPage

@allure.feature("browser search function")
class TestBaidu:
    """测试Baidu"""

    test_data = Constants().load_yaml('baidu', path=Constants.TEST_DATA_DIR)

    def setup(self):
        print('set  up ----')
        try:
            # jenkins参数配置--是否无界面运行
            runenv = os.environ["using_headless"]
        except:
            # 没有配置using_headless，默认打开浏览器运行
            runenv = False
        self.driver = Constants().driver(self.test_data['search1']['browser'], runenv=runenv)

    def teardown(self):
        print('teardown --====')
        self.driver.quit()

    @pytest.mark.baidusearch
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("value", list(test_data['search1'].values())[2:], ids=['selenium', '元宵节', '元旦节'])
    def test_baidu_search(self, value):
        """测试搜索功能"""
        url = self.test_data['search1']['url']
        # 浏览器兼容性
        expect_value = MainPage(self.driver).search_function(value, url, "MainPage1")
        assert "百度为您找到相关结果约" in expect_value, "页面搜索失败！"


    @pytest.mark.bingsearch
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("value", list(test_data['search2'].values())[2:], ids=['GitHub', 'pytest', 'diffy'])
    def test_bing_search(self, value):
        """测试搜索功能"""
        url = self.test_data['search2']['url']
        # 浏览器兼容性
        expect_value = MainPage(self.driver).search_function(value, url, "MainPage2")
        assert "Results" in expect_value, "页面搜索失败！"

    @pytest.mark.sosearch
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("value", list(test_data['search3'].values())[2:], ids=['swagger', 'YAPI', 'openstf'])
    def test_360_search(self, value):
        """测试搜索功能"""
        url = self.test_data['search3']['url']
        # 浏览器兼容性
        expect_value = MainPage(self.driver).search_function(value, url, "MainPage3")
        assert "找到相关结果约" in expect_value, "页面搜索失败！"

    @pytest.mark.xfail()
    @pytest.mark.run(order=4)
    def test_dont_count_fail(self):
        a = 5
        b = 7
        assert a == b

    @pytest.mark.skip(reason="本迭代不涉及")
    @pytest.mark.run(order=2)
    def test_skip(self):
        print("直接跳过不执行")

    @allure.story("test fixture")
    def test_fixture(self, sessionfix):
        fixture = "fixture"
        assert sessionfix == fixture

    @allure.story("注册失败")
    def test_register_failure(self):
        with allure.step("输入用户名"):
            print("输入用户名")

        with allure.step("输入密码"):
            print("输入密码")

        with allure.step("再次输入密码"):
            print("再次输入密码")

        print("点击注册")
        with allure.step("注册失败"):
            print("注册失败")

if __name__ == "__main__":
    pytest.main()

