"""
包 用来管理 模块
组成：一些模块 + ——init__.py文件
导包方式：
    方式一：import 包名.模块名
        调用： 包名.模块名.函数名()
    方式二:from 包名 import 模块名
        调用：模块名.函数名()
"""

import my_package.my_module1
my_package.my_module1.get_sum(1,2)
my_package.my_module1.fun01()

from my_package import my_module1
my_module1.get_sum(1,4)
my_module1.fun01()


from my_package import*
my_module1.fun01()
my_module2.fun01()
# my_module3.fun01()  #报错，all属性里面没有导入my_module3模块

