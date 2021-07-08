"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Constant
@time: 2020/12/30 23:55
@desc: 固定参数值
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
import os
from venv import logger

import yaml
from selenium import webdriver


class Constants:
    """固定参数"""

    ROOT_PATH = os.path.realpath(__file__).split("BasePage")[0]
    DATA_DIR = os.path.join(ROOT_PATH, "Data")
    PAGE_ELE_DIR = os.path.join(DATA_DIR, 'PageElement')
    TEST_DATA_DIR = os.path.join(DATA_DIR, 'TestData')


    def load_yaml(self, project_name, module_name=None, path=PAGE_ELE_DIR):
        """加载配置文件"""
        DATA_PATH = os.path.join(path, f"{project_name}.yaml")
        try:
            with open(DATA_PATH, encoding='utf-8') as temp:
                datas = yaml.safe_load(temp)
            data = datas.get(module_name, None)

            return data if data else datas

        except:
            logger.error(F"此文件{DATA_PATH}不存在")


    def driver(self, broswer):
        """获取浏览器驱动"""
        browser_map = {
            "chrome": "Chrome",
            "fixfore": "Firefox",
            "safari": "Safari",
            "ie": "Ie"
            }
        broswer = browser_map.get(broswer.lower(), '')
        if hasattr(webdriver, broswer):
            return getattr(webdriver, broswer)()
        else:
            raise Exception(f"不支持该浏览器：{broswer}")



if __name__ == "__main__":
    y = Constants().load_yaml('baidu','')
    print(y)


