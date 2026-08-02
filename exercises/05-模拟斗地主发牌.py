import random
#模拟斗地主发牌
poker_dic = {}
poker_num = []
p1 = []
p2 = []
p3 = []
dp = []
# 点数对应编号
num_map = {
    0:"3",1:"4",2:"5",3:"6",4:"7",5:"8",6:"9",7:"10",
    8:"J",9:"Q",10:"K",11:"A",12:"2",13:"小王",14:"大王"
}
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
    for i in range(len(poker_num)):
        if i >= len(poker_num) - 3:
            dp.append(poker_num[i])
        elif i % 3 ==0:
            p1.append(poker_num[i])
        elif i % 3 ==1:
            p2.append(poker_num[i])
        else:
            p3.append(poker_num[i])

# 看牌
def look_poker():
    def trans(cards):
        return [num_map[x] for x in sorted(cards)]
    print("玩家1：", trans(p1))
    print("玩家2：", trans(p2))
    print("玩家3：", trans(p3))
    print("底牌：", trans(dp))


if __name__ == '__main__':
    get_poker()
    shuffle_poker()
    deal_poker()
    look_poker()

# 没有解决花色问题
