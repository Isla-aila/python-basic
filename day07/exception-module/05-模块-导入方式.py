"""
模块介绍：
    概述：
        模块指的是Module,再Python中，1个 .py文件 = 1个模块
        可以把模块理解为工具包，工具包中有很多工具，其实就是：每个 .py文件 中都有很多的函数，这些函数都有不同的功能
    学模块就是记一些 .py文件，以及其中的一些函数
    例如：随机数相关使用 random模块，  日期相关用time模块，文件路径相关用os模块...

    模块的导入方式:                                        调用方式：
    方式1：import 模块名                                模块名.函数名()     模块下所有函数均可使用
    方式2：import 模块名 as 别名                         别名.函数名()       模块下所有函数均可使用
    方式3：from 模块名 import函数名                      函数名()           只能使用该模块下导入到函数
    方式4：from 模块名 import函数名 as 别名              别名()             只能使用该模块下导入到函数
    方式5：from 模块名 import*                          函数名()             模块下所有函数均可使用
"""

# 测试用例time 模块下的time()函数，sleep()函数

# 演示方式1：import 模块名                                模块名.函数名()     模块下所有函数均可使用

# import time
# print('---start---')
# time.sleep(2)           #让程序休眠 2秒
# print(time.localtime()) #获取系统的本地时间
# print(time.time())      #1784890341.3809736，从时间原点（1970年1月1日00：00：00）到现在的秒值
# print('---end---')

# 演示方式2：import 模块名 as 别名                         别名.函数名()       模块下所有函数均可使用

# import time as t
# print('---start---')
# t.sleep(2)                #让程序休眠 2秒
# print(t.localtime())      #获取系统的本地时间
# print(t.time())           #1784890341.3809736，从时间原点（1970年1月1日00：00：00）到现在的秒值
# print('---end---')

# 演示方式3：from 模块名 import函数名                      函数名()           只能使用该模块下导入到函数

# from time import sleep,localtime,time
# print('---start---')
# sleep(2)                  #让程序休眠 2秒
# print(localtime())        #获取系统的本地时间
# print(time())             #1784890341.3809736，从时间原点（1970年1月1日00：00：00）到现在的秒值
# print('---end---')

# 演示方式4：from 模块名 import函数名 as 别名              别名()             只能使用该模块下导入到函数

# from time import sleep,localtime as lt,time as t
# print('---start---')
# sleep(2)            #让程序休眠 2秒
# print(lt())         #获取系统的本地时间
# print(t())          #1784890341.3809736，从时间原点（1970年1月1日00：00：00）到现在的秒值
# print('---end---')

# 演示方式5：from 模块名 import*                          函数名()             模块下所有函数均可使用
from time import *
print('---start---')
sleep(2)                  #让程序休眠 2秒
print(localtime())        #获取系统的本地时间
print(time())             #1784890341.3809736，从时间原点（1970年1月1日00：00：00）到现在的秒值
print('---end---')