"""
1、小兔子一个月会长成大兔子
2、1对大兔子每个月会生一对小兔子
3、假设所有兔子的不死，按照此模式。那么第一个月有1对小兔子,一年之后会变成多少对兔子
"""
# month 1   2   3   4   5   6   7   8   9   10
# big   0   1   1   2   3   5   8   13
# small 1   0   1   1   2   3   5   8
# all   1   1   2   3   5   8   13

def get_rabbit(m):
    """
    传入月份，计算兔子对数
    :param m:几个月
    :return: 当月兔子对数
    """
    # 前两个月(出口
    if m == 1 or m == 2:
        return 1
    else:
        return get_rabbit(m - 1) + get_rabbit(m - 2)    #规律

if __name__ == '__main__':
    print(get_rabbit(12))