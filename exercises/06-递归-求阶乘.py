"""
递归
    1.必须要有出口，否则：就是四递归，容易造成 栈内存溢出
    2.递归不能调用次数过多
    3.递归必须有 规律
"""

# 需求：求5的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)






if __name__ == '__main__':
    print(factorial(5))

