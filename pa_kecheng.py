# coding:utf-8
#很多时候我们无法直接定位到某个元素，我们可以先定位它的父元素，通过父元素来找子元
# 素就比较容易


#contents 获取所有字节点
from bs4 import BeautifulSoup
import requests
import re
import os
import random
import time

r=requests.get("http://www.cnblogs.com/yoyoketang/")
# 请求首页后获取整个 html 界面
html = r.content
# 用 html.parser 解析 html
soup = BeautifulSoup(html, "html.parser")
# find 方法查找页面上第一个属性匹配的 tag 对象
# tag_zaiyao =soup.find(class_="c_b_p_desc")
# # #len 函数获取子节点的个数
# print(len(tag_zaiyao.contents))
# # #len 函数获取子节点的个数 children 为list对象
# print(len(list(tag_zaiyao.children)))

# #循环打印出子节点
# for i in tag_zaiyao.contents:
#     print(i)

# # 循环打印出子节点 .children 一般上面那个 contents 用的比较多，可能 children 性能更快吧，我猜想的嘿嘿！）
# for i in tag_zaiyao.children:
#     print(i)
    
# # 通过下标取出第 1 个 string 子节点
# print (tag_zaiyao.contents[0])
# # 通过下标取出第 2 个 a 子节点
# print (tag_zaiyao.contents[1])

# 1.上面的 contents 只能获取该元素的直接子节点，如果这个元素的子节点又有子节点（也
# 就是孙节点了），
# 这时候获取所有的子孙节点就可以用.descendants 方法
# 获取子孙节点的个数
# print (len(list(tag_zaiyao.descendants)))
# for i in tag_zaiyao.descendants:
# 	print (i)



tag_titles=soup.find_all(class_="postTitle2")

tag_times=soup.find_all(title="Day link")
time2=time.strftime("%Y%m%d%H%M%S",time.localtime())
for h,i in zip(tag_times,tag_titles):
	time=re.search(">(.+?)</a>", str(h))
	title = re.search(">(.+?)</a>", str(i))
	url = i['href']
	print(time.group(1)+title.group(1))
	print(url)
	# c=random.randint(1,10)
	with open(os.getcwd()+"\\yoyo_kecheng\\"+time2+".txt","a+",encoding='utf-8')  as f:
		f.write(time.group(1)+title.group(1)+'\n')
		f.write(url+'\n')

# for i in tag_titles:
# 	url=i['href']
#     # title=re.search(">(.+?)-(.+?)</a>",str(i))  #使用re.search()正则匹配时间及title  i.string 是对象属性，str(i)是把对象转成str
#     title = re.search(">(.+?)</a>", str(i))
#     print(title.group(1))  #跟jmeter的正则匹配一样的，匹配出来的东西是一个类似数组list一样的对象，需要从里面用group(n)去索引出来 group(0)取全部
#     print(url)



