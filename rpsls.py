#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������ʦ  ���ַ�
���ڣ�2019.11.20
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_human_to_number_human(name_human):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    
    if name_human=="ʯͷ":
      name_human=int(0)
    elif name_human=="ʷ����":
      name_human=int(1)
    elif name_human=="��":
      name_human=int(2)
    elif name_human=="����":
      name_human=int(3)
    elif name_human=="����":
      name_human=int(4)
    else:
      print("Error:No Correct Name")

    return name_human


def number_computer_to_name_computer(number_computer):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
	
    if number_computer==int(0):
      number_computer="ʯͷ"
    if number_computer==int(1):
      number_computer="ʷ����"
    if number_computer==int(2):
      number_computer="��"
    if number_computer==int(3):
      number_computer="����"
    if number_computer==int(4):
      number_computer="����"
    return number_computer



def rpsls(name_human):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
	
    print("����ѡ���ǣ�%s"%name_human)
    number_human=name_human_to_number_human(name_human)
    number_computer=random.randint(0,4)
    if number_computer-number_human==1:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("����Ӯ�ˣ�")
    elif number_computer-number_human==2:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("����Ӯ�ˣ�")
    elif number_computer-number_human==-3:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("����Ӯ�ˣ�")
    elif number_computer-number_human==-4:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("����Ӯ�ˣ�")
    elif number_computer==number_human:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("���ͻ�������һ���أ�")
    elif number_human-number_computer==1:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("��Ӯ�ˣ�")
    elif number_human-number_computer==2:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("��Ӯ�ˣ�")
    elif number_human-number_computer==-3:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("��Ӯ�ˣ�")
    elif number_human-number_computer==-4:
      name_computer=number_computer_to_name_computer(number_computer)
      print("�������ѡ��Ϊ��%s"%name_computer)
      print("��Ӯ�ˣ�")
		



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
name_human=input()
if name_human not in["ʯͷ","ʷ����","��","����","����"]:
    print("Error:No Correct Name") 
    print("----------------")
else:
    rpsls(name_human)
    print("----------------")
