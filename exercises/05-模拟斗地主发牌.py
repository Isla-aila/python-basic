import random
#模拟斗地主发牌
poker_dic = {}
poker_num = []
p1 = []
p2 = []
p3 = []
dp = []
#1.获取牌
def get_poker():
    # 定义花色列表、
    color_list = ['♠','♥','♦','♣']
    # 定义点数列表
    num_list = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    # 生成字典，键：牌 值：索引
    poker_list = [color + num for num in num_list for color in color_list]
    count,index =1,0
    for i in poker_list:
        poker_dic[i] = index
        if  count % 4 == 0:
            index += 1
        count +=1
    poker_dic['小王'] = 13
    poker_dic['大王'] = 14
    # 返回扑克牌字典
    print(poker_list)
    print(poker_dic)
# 洗牌
def shuffle_poker():
    global poker_num
    poker_num = list(poker_dic.values())
    random.shuffle(poker_num)
    return poker_num

# 发牌
def deal_poker():
    global p1, p2, p3, dp
        #后3张作为底牌


if __name__ == '__main__':
    get_poker()
    # print(poker_dic)
    shuffle_poker()
    print(poker_num)
