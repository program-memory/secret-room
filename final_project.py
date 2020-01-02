#encoding:gbk
"""
程序：对《黎明破晓的街道》文本中人物关系的提取,利用Gelphi软件对人物关系可视化
作者：池林峰  Doctor.CHI
"""


import os,sys
import jieba,codecs,math
import jieba.posseg as pseg


names={} 
relationships={} 
lineNames=[]  
jieba.load_userdict('dict.txt')  #将小说人物录入字典
with codecs.open("黎明破晓的街道1.txt",'r',encoding='utf-8') as f:  #对文本进行筛选处理
    for line in f.readlines():  #对每一段话进行人物筛选
        poss=pseg.cut(line)
        lineNames.append([])
        for w in poss:     #在字段中进行人名筛查，对于不符合人名规则的字符不进行筛查
            if  w.flag!="nr" or len(w.word) <2:  
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1


for line in lineNames:  #对于人物关系重要性进行加权，体现出人物之间的重要性
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
with codecs.open('2.txt','w','gbk') as f:    #将人物关系重要性写入文本文档中
    f.write("source target weight\r\n")
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w>3:
                f.write(name+ " "+v+" "+str(w)+"\r\n")
