"""
已知有1，2，3，4四个数字，问：他们能组合成的四位数有哪些，并打印到控制台
需求：
    1.数字不能重复，例 ：1213不行
    2.实现：1和3不能连续
    3.数字4不能首位
    4.代码不超过7行
"""
count = 0
for i in range(1234,4322):
    s = str(i)
    if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4':
        count += 1
        print(i,end ='\n' if count % 3 == 0 else '\t')