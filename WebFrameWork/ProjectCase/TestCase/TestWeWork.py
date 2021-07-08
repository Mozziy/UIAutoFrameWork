"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: TestWeWork
@time: 2020/12/26 22:03
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

from WebFrameWork.BasePage.Constant import Constants
from WebFrameWork.PageObject.Wework.AddMemberPage import AddMemberPage

from WebFrameWork.PageObject.Wework.LoginPage import LoginPage


class TestWeWork:
    """测试企业微信"""


    def setup_class(self):
        self.datas = Constants().load_yaml("WeWork", path=Constants.TEST_DATA_DIR)
        self.driver = Constants().driver(self.datas['login']['browser'])
        self.url = self.datas['login']['url']
        self.login = LoginPage(self.driver)
        self.login.login_main(self.url)

    def teardown_class(self):
        pass

    def test_login_to_login(self):
        """扫码登录"""
        res = self.login.go_to_scan()
        assert "企业微信扫码登录" in res, "登录失败"
        self.driver.back()

    def test_login_to_register(self):
        """注册"""
        res = self.login.go_to_register()

    def test_add_member(self):
        """添加成员"""
        data = self.datas['add_member']
        cookies = data['cookies']
        add_nam_val = data['add_nam_val']
        add_snam_val = data['add_snam_val']
        add_cid_val = data['add_cid_val']
        add_phone_no = data['add_phone_no']
        res = AddMemberPage().add_member(cookies, add_nam_val, add_snam_val, add_cid_val, add_phone_no)
        print(res)
        assert res == 19





