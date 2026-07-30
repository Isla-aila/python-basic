"""
    try:
        里面写的是可能出问题的代码
    except [Exception as e]:
        出现问题后的 解决方案
    else:
        只要try中内容无问题，直接会执行这里的内容
        只要try中有问题，就会跳过这里的代码
    finally:
        无论try是否有问题，都会走这里，一般用于释放资源
"""
"""
try:
    print('try1')
    print(10//0)
    print('try2')
except Exception as e:
    print(f'程序出问题了',{e})
    print('else执行了')
finally:
    print('finally执行了')
"""


# try:
#     print('try1')
#     print(10//5)
#     print('try2')
#     print('else执行了')
# except Exception as e:
#     print(f'程序出问题了',{e})
#
# finally:
#     print('finally执行了')

try:
    fr = open('1.txt', 'rb')
    fw = open('2.txt', 'wb')
except Exception as e:
    print(f'出问题了',{e})
else:
    while True:
        data = fr.read(1024*8)
        if len(data) <= 0:
            break
        fw.write(data)
    print('完成')
finally:
    try:
        fr.close()
    except Exception as e:
        print({e})

    try:
        fw.close()
    except Exception as e:
        print({e})


try:
    with open('1.txt', 'rb') as fr,open('2.txt', 'wb') as fw:
        while True:
            data = fr.read(1024*8)
            if len(data) <= 0:
                break
            fw.write(data)
        print('完成')
        fr.close()
        fw.close()
except Exception as e:
    print({e})








