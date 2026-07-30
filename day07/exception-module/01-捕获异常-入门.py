try:
    print('try1')
    src_f = open('1.txt', 'r')
    print('try2')
except:
    print('文件不存在，请校验后重新操作')
print('看看我执行了吗')