#encoding:gbk
"""
���򣺶ԡ����������Ľֵ����ı��������ϵ����ȡ,����Gelphi����������ϵ���ӻ�
���ߣ����ַ�  Doctor.CHI
"""


import os,sys
import jieba,codecs,math
import jieba.posseg as pseg


names={} 
relationships={} 
lineNames=[]  
jieba.load_userdict('dict.txt')  #��С˵����¼���ֵ�
with codecs.open("���������Ľֵ�1.txt",'r',encoding='utf-8') as f:  #���ı�����ɸѡ����
    for line in f.readlines():  #��ÿһ�λ���������ɸѡ
        poss=pseg.cut(line)
        lineNames.append([])
        for w in poss:     #���ֶ��н�������ɸ�飬���ڲ���������������ַ�������ɸ��
            if  w.flag!="nr" or len(w.word) <2:  
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1


for line in lineNames:  #���������ϵ��Ҫ�Խ��м�Ȩ�����ֳ�����֮�����Ҫ��
   for name1 in line:
      for name2 in line:
          if name1==name2:
              continue
          if relationships[name1].get(name2) is None:
            relationships[name1][name2]=1
          else:
            relationships[name1][name2]+=1

with codecs.open('1.txt','w','gbk') as f:
    f.write("id lable weight\r\n")
    for name,times in names.items():
        f.write(name+" "+name+" "+str(times)+"\r\n")
with codecs.open('2.txt','w','gbk') as f:    #�������ϵ��Ҫ��д���ı��ĵ���
    f.write("source target weight\r\n")
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w>3:
                f.write(name+ " "+v+" "+str(w)+"\r\n")
