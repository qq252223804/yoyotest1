#coding:utf-8
import logging,time,os
'''创建logger
创建handler
定义formatter
给handler添加formatter
给logger添加handler
'''
# 这个是日志保存本地的路径
log_path='E:\\yoyotest\\log'
# print(log_path)
class Log:
	def __init__(self):
		#文件的命名     #os.path.join用法：将多个路径组合后返回os.path.join(path1[,path2[,path3[,...[,pathN]]]])
		self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d_%H_%M'))
		self.logger=logging.getLogger()
		# Logger是Logging模块的主体，进行以下三项工作：
		# 1.为程序提供记录日志的接口
		# 2.判断日志所处级别，并判断是否要过滤
		# 3.根据其日志级别将该条日志分发给不同handler
		
		#      另外你也可以通过日志名称来区分同一程序的不同模块，比如这个例子。
		# self.logger=logging.getLogger('App.ui')
		# self.logger = logging.getLogger('App.service')
	
		
		#日志输出格式
		self.formatter=logging.Formatter('[%(asctime)s]- %(filename)s]- %(levelname)s: %(message)s')

		# 建立一个filehandler来把日志记录在文件里，级别为debug以上
		fh=logging.FileHandler(self.logname,'a',encoding='utf-8')
		# 设置日志级别,格式
		self.logger.setLevel(logging.DEBUG)
		fh.setFormatter(self.formatter)   #设定的fh应用到日志输出格式中
		self.logger.addHandler(fh)    #把filehandler添加到logger主体中
		
		# 建立一个streamhandler来把日志打在CMD窗口上，级别为debug以上
		ch = logging.StreamHandler()
		# 设置日志级别,格式
		self.logger.setLevel(logging.DEBUG)
		ch.setFormatter(self.formatter)
		self.logger.addHandler(ch)     #把streamhandler添加到logger主体中
		# print('ceshi')
	
	# 这两行代码是为了避免日志输出重复问题
	# 	self.logger.removeHandler(ch)
	# 	self.logger.removeHandler(fh)
		# 关闭打开的文件
		fh.close()
	def getlog(self):
		return self.logger
	def info(self, message):
		self.logger.info( message)
	def debug(self, message):
		self.logger.debug( message)
	
	def warning(self, message):
		self.logger.warning( message)
	
	def error(self, message):
		self.logger.error( message)
	
	def critical(self, message):
		self.logger.critical( message)

if __name__ == "__main__":
	log = Log()
	log.info("一个info信息")
	log.debug("一个debug信息")
	log.warning("一个waring信息")
	log.error('一个error信息')
	log.critical('一个致命critical信息')
	print(time.strftime('%Y-%m-%d %H:%M:%S'))
