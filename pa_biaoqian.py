import requests
from bs4 import BeautifulSoup
import os
import time
r=requests.get("http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang")
html=r.content
soup=BeautifulSoup(html,"html.parser")
#先定位父元素：<div class="catListTag">
tag_biaoqians=soup.find(class_="catListTag")
# print(len(list(tag_biaoqians.children)))
# # for i in tag_biaoqians:
# # 	print(i)
# for h in tag_biaoqians.descendants:
# 	print (h)


biaoqian=tag_biaoqians.find_all('a')
time2=time.strftime("%Y%m%d%H%M%S",time.localtime())
# print(biaoqian)
for i in biaoqian:
	print(i)
	# print(i['href'])
	with open(os.getcwd() + "\\yoyo_biaoqian\\" + time2 + ".txt", "a+", encoding='utf-8')  as f:

		f.write(str(i)+'\n')
