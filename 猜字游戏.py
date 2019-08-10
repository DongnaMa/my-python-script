import random
#随机生成1~10整数
secret = random.randint(1, 10)
print('.................我爱python.................')
temp = input("不妨猜一下我现在心里想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("好厉害！猜对啦！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~")
        else:
            print("嘿，小了，小了~~")
print("游戏结束，不玩啦！")
