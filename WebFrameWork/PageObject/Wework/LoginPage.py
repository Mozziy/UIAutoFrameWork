"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: LoginPage
@time: 2021/1/2 12:54
@desc:
"""


from WebFrameWork.BasePage.BasePage import BasePage
from WebFrameWork.BasePage.Constant import Constants
from WebFrameWork.PageObject.Wework.RegisterPage import RegisterPage


class LoginPage(BasePage):
    """登录页面"""

    login = Constants().load_yaml('WeWork', 'login')

    def login_main(self, url):
        """测试登录功能"""
        self.open_browser(url)

    def go_to_scan(self):
        """跳转到扫码登录页面"""
        print(self.login["login_loc"])
        self.click(self.login["login_loc"])
        # 因用cookie登录，所以这里跳过了，不在返回页面
        return self.driver.page_source

    def go_to_register(self):
        """跳转到注册页面"""
        self.click(self.login['register_loc'])
        return RegisterPage()
