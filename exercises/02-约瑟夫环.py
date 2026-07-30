#1.录入参与游戏的总人数，并接收
num = int(input('请录入参与游戏的总人数：'))
#2.根据总人数，生成对应的编号列表， 即[1,2,3,4,5 ...,num]
num_list = [i for i in range(1,num+1)]
# print(num_list)

# 定义两个变量，num表示当前数到的数字，i表示当前这个人的编号(索引)
num,i = 0,0
#具体的游戏过程，循环操作，直至列表剩下一个元素
while len(num_list) >1:
    num +=1
    # 如果一圈都数完了，重置索引为0，从头继续数
    if len(num_list)-1 == i:
        i = -1
# 如果当前数列的数字是3或3的倍数，就从列表中删除这个元素
    if num / 3 == int(num / 3):
        del num_list[i]
        i -=1

    i +=1

# 只剩下一个元素，该元素即为幸运元素
print(num_list[0])







