"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: FakerGenerator.py
@time: 2021/1/2 17:35
@desc: 数据生成器
 * * * * * * 幸运女神保佑 * * * * * 永无BUG * * * * * * * * * * * * *
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
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

"""
import random

from faker import Faker

class FakerGenerator:
    """数据生成器"""

    def __new__(cls, value):

        cls._list = value.split('_')[1:]
        cls._Faker = Faker()

        if len(cls._list) >= 3:
            raise Exception("目前只支持此类型[e:英文]: random-数据类型-长度/e")

        elif len(cls._list).__eq__(1) or cls._list[-1].__ne__('e'):
            cls._Faker = Faker('zh_CN')

        if hasattr(cls._Faker, cls._list[0]):
            return getattr(cls._Faker, cls._list[0])()

        elif hasattr(FakerGenerator, cls._list[0]):
            return getattr(FakerGenerator, cls._list[0])(cls, cls._list[1]) if len(cls._list)>1 \
                else getattr(FakerGenerator, cls._list[0])(cls)



    def trxId(cls, length=8):
        """获取流水号"""
        return cls._Faker.iban()[:int(length)]


    def phone(cls, length=0):
        """生成手机号或验证码"""
        return cls._Faker.phone_number() if not length \
            else str(random.randint(1000000000, 9999999999))[:int(length)]

