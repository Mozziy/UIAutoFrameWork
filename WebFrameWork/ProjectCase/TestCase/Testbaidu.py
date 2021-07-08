"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Testbaidu
@time: 2020/12/30 23:50
@desc:
              幸运女神保佑        永无BUG
 *
 *                      .::::.
 *                    .::::::::.
 *                   :::::::::::
 *                ..:::::::::::'
 *             '::::::::::::'
 *               .::::::::::
 *          '::::::::::::::..
 *               ..::::::::::::.
 *             ``::::::::::::::::
 *              ::::``:::::::::'        .:::.
 *             ::::'   ':::::'       .::::::::.
 *           .::::'      ::::     .:::::::'::::.
 *          .:::'       :::::  .:::::::::' ':::::.
 *         .::'        :::::.:::::::::'      ':::::.
 *        .::'         ::::::::::::::'         ``::::.
 *    ...:::           ::::::::::::'              ``::.
 *   ```` ':.          ':::::::::'                  ::::..
 *                      '.:::::'                    ':'````..
"""

import pytest
from WebFrameWork.BasePage.Constant import Constants
from WebFrameWork.PageObject.BaiduMainPage.MainPage import MainPage


class TestBaidu:
    """测试Baidu"""

    test_data = Constants().load_yaml('baidu', path=Constants.TEST_DATA_DIR)
    search_function = test_data["search_function"]

    @pytest.mark.parametrize("value", list(search_function.values())[2:])
    def test_research(self, value):
        """测试搜索功能"""
        # 固定的，未找到如何不用传参——写死？？？？ TODO
        url = self.search_function['url']
        # 浏览器兼容性
        driver = Constants().driver(self.search_function['browser'])
        expect_value = MainPage(driver).search_function(value, url)
        assert "百度为您找到相关结果约" in expect_value, "页面title属性值错误！"


if __name__ == "__main__":
    pytest.main()
