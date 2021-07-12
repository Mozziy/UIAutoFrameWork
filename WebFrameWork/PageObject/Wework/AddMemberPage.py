"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: AddMemberPage.py
@time: 2021/1/2 20:38
@desc:


"""


from WebFrameWork.BasePage.BasePage import BasePage
from WebFrameWork.BasePage.Constant import Constants
from WebFrameWork.PageObject.Wework.ContactPage import ContactPage


class AddMemberPage(BasePage):
    """添加成员界面"""

    AddMember = Constants().load_yaml('WeWork', 'addmember')

    def add_member(self, cookies, add_nam_val, add_snam_val, add_cid_val, add_phone_no):
        """测试增加成员"""
        self.open_browser(self.AddMember['url'])
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.open_browser(self.AddMember['url'])
        self.click(self.AddMember['add_btn_loc'])
        self.send_keys(self.AddMember['add_nam_loc'], add_nam_val)
        self.send_keys(self.AddMember['add_snam_loc'], add_snam_val)
        self.send_keys(self.AddMember['add_cid_loc'], add_cid_val)
        self.click(self.AddMember['gender_loc'])
        self.send_keys(self.AddMember['add_phone_loc'], add_phone_no)
        self.click(self.AddMember['save_btn_loc'])
        return ContactPage(self.driver).get_number_list()




