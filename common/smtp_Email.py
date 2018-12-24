# coding:utf-8
import smtplib
from email.mime.text import MIMEText         #发送文本模块
from email.mime.multipart import MIMEMultipart # 发送附件模块
from common.logger import Log


def send_email():
	# ----------1.跟发件相关的参数------
	# smtpserver  # 发件服务器
	smtpserver = "smtp.qq.com"
	port = 465 # 端口
	sender = "252223804@qq.com" # 账号
	shouquan = "jnjorpipnagsbggi" # 授权码  qq邮箱
	receiver = ["252223804@qq.com","563024145@qq.com"] # 接收人

	# ----------2.编辑邮件的内容------
	#读文件
	file_path =('E:\\yoyotest\\report\\result.html')
	with open (file_path,'rb') as fb:
		mail_body=fb.read()
	# body='<p>这个是发送的个人自动化邮件</p>'
	subject="主题:阿健测试报告"
	msg = MIMEMultipart()
	msg['from'] = sender
	msg['to'] = ";".join(receiver)  #发送多个接收人
	msg['subject'] =subject
	#正文
    # 定义邮件正文为 html 格式
	body = MIMEText(mail_body, "html", "utf-8")
	msg.attach(body)
#
# 	#附件
	att=MIMEText(mail_body,'base64','utf-8')
	att["Content-Type"] = "application/octet-stream"
	att["Content-Disposition"] = 'attachment; filename="test_report.html"' #重命名的邮件
	msg.attach(att)
#
#
# 	# ----------3.发送邮件163------
	# smtp = smtplib.SMTP()
	# smtp.connect(smtpserver)  # 连服务器
	try:
		# # ----------4.发送邮件QQ------
		smtp = smtplib.SMTP_SSL(smtpserver, port)
		smtp.login(sender, shouquan) # 登录

		smtp.sendmail(sender, receiver, msg.as_string()) # 发送
		smtp.quit() # 关闭
	except Exception as e:
		# print(e)
		Log().warning('邮件发送失败:%s'%e)

send_email()



# coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# # ----------1.跟发件相关的参数------
# # smtpserver = "smtp.163.com" # 发件服务器
# smtpserver = "smtp.qq.com"
# port = 465 # 端口
# sender = "252223804@qq.com" # 账号
# psw = "jnjorpipnagsbggi" # 密码
# receiver = "1052252939@qq.com" # 接收人
# # ----------2.编辑邮件的内容------
# subject = "这个是主题QQ2"
# body = '<p>这个是发送的 QQ 邮件</p>' # 定义邮件正文为 html 格式
# msg = MIMEText(body, "html", "utf-8")
# msg['from'] = sender
# msg['to'] = "1052252939@qq.com"
# msg['subject'] = subject
# # ----------3.发送邮件------
# # smtp = smtplib.SMTP()
# # smtp.connect(smtpserver) # 连服务器
# smtp = smtplib.SMTP_SSL(smtpserver, port)
# smtp.login(sender, psw) # 登录
# smtp.sendmail(sender, receiver, msg.as_string()) # 发送
# smtp.quit() # 关闭



# 1.Subject 和正文内容不要用 hello、hehe、test 等单词
# 2.from(发件人)和 to(收件人)不要为空，
# （要不然会被认为是垃圾邮件）
# 3.找不到的话，先看下垃圾信箱，是不是跑到垃圾箱了
# 4.如果前几次可以收到，后来收不到了，需改下 subject 内容
# （因为每次都是一个 subject，系统也会拒收的，把 subject 内容设置为动态
# 的是最好的）
# 5.部分邮箱是 ssl 加密了的，所以无法发送，如:qq 邮箱
# （用授权码去登录）
# 6.要是按照上面的步骤来报错了，说明 代码抄错了，多检查几次。
# (以上代码在 python2 和 python3 上都测试通过了）