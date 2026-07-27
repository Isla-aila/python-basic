
def get_sum(a,b):
    """
    该函数用于两数相加求和
    :param a: 值1
    :param b: 值2
    :return: a+b
    """
    print('我是 my_module1模块的函数')
    print(__name__)
    return a+b

def fun01():
    print('我是 my_module1模块的函数')
    print('----fun01函数----')
    print(__name__)

def fun02():
    print('我是 my_module1模块的函数')
    print('----fun02函数----')
    print(__name__)


# 实际开发中定义好模块后,一般会对模块功能(函数)做测试
# 如下的测试代码,在调用者中也会被执行,但真实的业务场景中不能被执行
# 如何解决
# 答案:__name__属性 即可解决这个事,在当前模块中打印的结果是__main__,
#                               在调用者模块中打印的结果是当前模块名
# 测试代码
# print(get_sum(1,3))
# fun01()
# fun02()

# 如果条件成立,说明是在当前模块中执行的
if __name__ == '__main__':
    print(get_sum(1, 3))
    fun01()
    fun02()
