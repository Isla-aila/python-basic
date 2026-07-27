"""
一个 .py文件就可以看作是一个模块,文件名 = 模块名,所有:文件名也要符合标识符的命名规范
"""
# 需求:自动有 my_module1模块,然后在其中定义一些函数,在当前模块中,调用mu_module1模块

import my_module1 as m1
import my_module2 as m2
m1.fun01()
m2.fun01()

# print(mo.get_sum(1, 3))
# m1.fun01()
# m1.fun02()

from my_module2 import*
fun01()
fun02()
# print(get_sum(1,5))





