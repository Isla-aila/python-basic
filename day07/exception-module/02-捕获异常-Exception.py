"""
    try:
        可能出问题的代码
    except Exception as e:
        出问题后的解决方案

细节：
    还可以写成 except(异常1，异常2) as e 捕获多个异常
"""
try:
    src_f = open('3.txt','r')     #FileNotFoundError
    # print(10//0)                  #ZeroDivisionError
    # print(name)                      #NameError
except Exception as e:
    print(e)

