"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: demo.py
@time: 2021/1/5
@desc:
"""
import pytest
from appium import webdriver

class TestDemo:

  def setup_class(self):

    self.desire_cap = {
      "platformName": "android",
      "platformVersion": "11.0",
      "appPackage": "com.xueqiu.android",
      "deviceName": "emulator-5554",
      "appActivity": ".view.WelcomeActivityAlias",
      "noReset": True,  # 记住之前的动作，不会清空之前操作的缓存
      # "dontStopAppOnReset": True   # 程序运行到哪个页面就在那个页面停止
    }
    self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
    self.driver.implicitly_wait(10)

  def teardown_class(self):
    self.driver.quit()

  def test1(self):

    # driver.find_element_by_id('com.xueqiu.android:id/tv_agree').click()
    el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
    el1.click()
    self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("alibaba")
    el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
    el2.click()







