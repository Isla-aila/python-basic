"""异常具有传递性，函数内的异常 会传递给发函数的 调用者，逐级传递，直至这个异常被处理，或传递到main,还不处理程序就会报错"""

# 案例：演示异常的传递性
def fun01():
    print('--------fun01 start--------')
    # try:
    print(1/0)
    # except Exception as e:
    #     print(e)
    print('---------fun01 end---------')
def fun02():
    print('--------fun02 start--------')
    # try:
    fun01()
    # except Exception as e:
    #     print(e)
    print('--------fun02 end--------')
def fun03():
    print('--------fun03 start--------')
    # try:
    fun02()
    # except Exception as e:
    #     print(e)
    print('--------fun03 end--------')
if __name__ == '__main__':
    try:
        fun03()
    except Exception as e:
        print(e)