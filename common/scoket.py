#coding:utf-8
# Socket编程之服务端代码：
import socket   #socket模块
# import commands   #执行系统命令模块
HOST='10.0.0.245'
PORT=50007
# (host='112.74.192.99 ',user='root',passwd='Ld123456BJ',db='test',port=3307,charset="utf8")
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))   #套接字绑定的IP与端口
s.listen(1)         #开始TCP监听,监听1个请求
while 1:
    conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
    print('Connectedby',addr) #输出客户端的IP地址

	# while 1:
    	# data=conn.recv(1024)    #把接收的数据实例化
    	# cmd_status,cmd_result=commands.getstatusoutput(data)   #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
     #    	if len(cmd_result.strip()) ==0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
     #            conn.sendall('Done.')
     #    	else:
     #            conn.sendall(cmd_result)   #否则就把结果发给对端（即客户端）
conn.close()     #关闭连接



# Socket编程之客户端代码
import socket
HOST='10.0.0.245'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
	cmd=raw_input("Please input cmd:")       #与人交互，输入命令
	s.sendall(cmd)      #把命令发送给对端
	data=s.recv(1024)     #把接收的数据定义为变量
	print (data)         #输出变量
	s.close() #关闭连接