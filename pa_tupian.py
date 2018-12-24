# coding:utf-8
import requests
from bs4 import BeautifulSoup
import os

r = requests.get("http://699pic.com/sousuo-218808-13-popular-all-0-all-all-1-0-0-0-0-0-0-all-all.html")
# 请求后获取整个 html 界面
text = r.content
# 用 html.parser 解析 html
soup = BeautifulSoup(text, "html.parser")
# 找出所有的标签 find_all
images = soup.find_all(class_="lazy")
# print images # 返回 list 对象
for i in images:
	jpg_url = i["data-original"]  # 获取 url 地址
	title = i["title"]  # 返回 title 名称
	print(title)
	print(jpg_url)
	print("")  # 打印空行
	# 取图片
	jpgs = requests.get(jpg_url).content  # 也就是说，如果你文本，可以通过r.text。
	# 如果想取图片，文件，则可以通过r.content。
	# 保存照片                               # （resp.json()返回的是json格式数据）
	with open(os.getcwd() + "\\jpg\\" + title + '.jpg', 'wb') as f:  # 拼接下载好的图片名，保证不覆盖尾部格式很重要
		f.write(jpgs)  # os.getcwd()这个方法可以获取当前脚本的路径


