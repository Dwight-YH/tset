
# 项目名称：自动贩卖机
# 建立时间：2020年2月16日
# 是否需要优化：需要优化

#coding:utf-8

price = 0
shop_list = [["tea",5],["redtea",3],["qishui",2],["guozhi",6]]
buy_list = []
print("===========自动贩卖机===========")
print("编号 商品 金额")
for num,shop in enumerate(shop_list):
    print(num+1,shop[0],shop[1])
print("按0退出服务")
print("================================")
salary = int(input("请输入消费余额:"))
if salary > 0 :
    while True:
        sum = int(input("请输入商品编号："))
        if sum == 0:
            print("      商品清单    ")      #需要优化清单
            print("===================")
            print("商品名称 数量 价格")
            for var in buy_list:
                print(var)
            print("您本次总共消费%s元,卡内余额为%s元。"%(price,salary))
            print("欢迎下次光临！")
            print("===================")
            break
        elif sum > 0 and sum <= len(shop_list) :
            if salary >= shop_list[sum-1][1]:
                print("%s购买成功！" % (shop_list[sum - 1][0]))
                salary -= shop_list[sum-1][1]
                print("本次消费%s元，卡上剩余%s元"%(shop_list[sum-1][1],salary))
                buy_list.append(shop_list[sum-1][0])
                price += shop_list[sum-1][1]
            else:
                print("您的卡上余额为%s元，无法购买此商品。"%(salary))
        else :
             print("商品不存在，请重新输入！")
else:
    print("余额不足，请先充值。")

