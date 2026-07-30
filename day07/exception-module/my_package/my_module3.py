
__all__ = ['fun01', 'fun02']
def get_sum(a,b):
    """
    该函数用于两数相加求和
    :param a: 值1
    :param b: 值2
    :return: a+b
    """
    print('我是 my_module2模块的函数')
    print(__name__)
    return a+b

def fun01():
    print('我是 my_module3模块的函数')
    print('----fun01函数----')
    print(__name__)

def fun02():
    print('我是 my_module3模块的函数')
    print('----fun02函数----')
    print(__name__)


# 测试代码

if __name__ == '__main__':
    print(get_sum(1, 3))
    fun01()
    fun02()
