# coding:utf-8

#1.爬糗事百科首页的段子
from bs4 import BeautifulSoup
import requests
import os
import time
import random
# c=random.randint(1,10)
# print(c)

r = requests.get("https://www.qiushibaike.com/")
text = r.text
# print(text)
soup = BeautifulSoup(text, "html.parser")

duanzi = soup.find_all(class_="content")
# time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
time2=time.strftime("%Y%m%d%H%M%S",time.localtime())

for i in duanzi:
# tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出
    duan = i.span.contents[0] # 取第一个
    print(duan)

    with open(os.getcwd()+"\\duanzi_text\\"+time2+".txt","a+",encoding='utf-8') as f: # .尾部格式很重要
        f.write(duan+'\n')                               #encoding 对保存的txt文本进行编码否则打不开
                               # r为仅读取 w为仅写入 a为仅追加
                               # r+为可读写两种操作 w+为可读写两种操作（会首先自动清空文件内容） a+为追加读写两种操作
                          # 以上三种操作方式均不可同时进行读写操作
      