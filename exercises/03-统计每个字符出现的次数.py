"""
需求：
    键盘录入1个字符串，并接收，统计其中每个字符的次数，并将结果打印到控制台上
"""

# 1.键盘录入1个字符串，并接受
s = input('请录入1个字符串，我来统计每个字符的次数:')
#2.定义字典，记录每个字符，及其 次数 ，字符做键，次数做值：'a':3
wc_dict = {}
# 3.遍历上述的字符串，获取到每个字符，充当字典的键
# 4.核心：判断字典中是否有这个键，有但将其次数 +1重新存储

#方式一：
for key in s:
    if key in wc_dict:
        wc_dict[key] += 1
    # 5.没有说明这个件是第一次出现，将其次数记录为1
    else:
        wc_dict[key] = 1

#三元运算符
# for key in s:
#     wc_dict[key] = wc_dict[key]+1 if key in wc_dict else 1

print(wc_dict)
