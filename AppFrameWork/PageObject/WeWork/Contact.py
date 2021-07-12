"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Contact.py
@time: 2021/2/21 下午11:01
@desc:

"""

class Contact:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements

    def contact(self, name=None, account=None, alias=None,
                phone=None, tele=None, email=None,
                address=None, duty=None):
        self.element = self.elements["Contact"]
        self.Locator.locator_element(self.element["click_add"]).click()
        self.Locator.click(self.element["click_hand"])
        self.Locator.send_keys(self.element["name_send"], name)
        self.Locator.send_keys(self.element["account_send"], account)
        self.Locator.send_keys(self.element["alias_send"], alias)
        self.Locator.click(self.element["click_sex"])
        self.Locator.click(self.element["choice_sex"])
        self.Locator.send_keys(self.element["phone_send"], phone)
        self.Locator.send_keys(self.element["tele_send"], tele)
        self.Locator.send_keys(self.element["email_send"], email)
        self.Locator.click(self.element["click_addre"])
        self.Locator.send_keys(self.element["addre_send"], address)
        self.Locator.click(self.element["clcik_ensu"])
        self.Locator.send_keys(self.element["duty_send"], duty)
        self.Locator.click(self.element["click_iden"])
        self.Locator.click(self.element["choice_iden"])
        self.Locator.locator_element(self.element["click_save"]).click()




