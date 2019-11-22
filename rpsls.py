#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：汪璇老师  池林峰
日期：2019.11.20
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_human_to_number_human(name_human):
    """
    将游戏对象对应到不同的整数
    """
    
    if name_human=="石头":
      name_human=int(0)
    elif name_human=="史波克":
      name_human=int(1)
    elif name_human=="布":
      name_human=int(2)
    elif name_human=="蜥蜴":
      name_human=int(3)
    elif name_human=="剪刀":
      name_human=int(4)
    else:
      print("Error:No Correct Name")

    return name_human


def number_computer_to_name_computer(number_computer):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
	
    if number_computer==int(0):
      number_computer="石头"
    if number_computer==int(1):
      number_computer="史波克"
    if number_computer==int(2):
      number_computer="布"
    if number_computer==int(3):
      number_computer="蜥蜴"
    if number_computer==int(4):
      number_computer="剪刀"
    return number_computer



def rpsls(name_human):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
	
    print("您的选择是：%s"%name_human)
    number_human=name_human_to_number_human(name_human)
    number_computer=random.randint(0,4)
    if number_computer-number_human==1:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("机器赢了！")
    elif number_computer-number_human==2:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("机器赢了！")
    elif number_computer-number_human==-3:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("机器赢了！")
    elif number_computer-number_human==-4:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("机器赢了！")
    elif number_computer==number_human:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("您和机器出的一样呢！")
    elif number_human-number_computer==1:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("您赢了！")
    elif number_human-number_computer==2:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("您赢了！")
    elif number_human-number_computer==-3:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("您赢了！")
    elif number_human-number_computer==-4:
      name_computer=number_computer_to_name_computer(number_computer)
      print("计算机的选择为：%s"%name_computer)
      print("您赢了！")
		



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
name_human=input()
if name_human not in["石头","史波克","布","蜥蜴","剪刀"]:
    print("Error:No Correct Name") 
    print("----------------")
else:
    rpsls(name_human)
    print("----------------")
