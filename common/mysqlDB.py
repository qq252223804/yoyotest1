#coding:utf-8
import pymysql
from common.logger import Log

# 打开数据库连接
# db = pymysql.connect(
# host="112.74.192.99",
# user="root",
# password="Ld123456BJ",
# db='test',
# port=3306,
# charset="utf8"
# )
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # # 使用 execute()  方法执行 SQL 查询
# # cursor.execute("SELECT VERSION()")
# #
# # # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# ##使用 fetchall() 方法获取单条数据.
# # datas =cursor.fetchall()
#
# # print("Database version : %s " % data)
#
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS student")
#
# # 创建表
# try:
# 	sql='''create table student(
# 	sno varchar(20)not null primary key,
# 	sname varchar(20)not null,
# 	ssex varchar(20)not null,
# 	sbirthday datetime not null,
# 	class varchar(20)not null
# 	) ;
# 	'''
# 	cursor.execute(sql)
# 	# 提交到数据库执行
# 	db.commit()
# 	print('ok')
# except pymysql.err.Error as e:
# # except Exception as e:
# 	# 如果发生错误则回滚
# 	db.rollback()
# 	print(e)
#
#
#
# # 插入与查找数据
# sql='''insert into student (sno,sname,ssex,sbirthday,class) values(%s,%s,%s,%s,%s);
# 	'''
# try:
# 	# rows变量得到数据库中被影响的数据行数。
# 	cursor.execute(sql, ('108','曾华','男','1977-09-01',95033))
# 	# 使用executemany()
# 	# 来多条插入信息。要用列表包含元组的形式插入。[(), (), ()]
# 	cursor.executemany(sql,[('105','匡明','男','1975-10-02',95031),
# 								 ('107','王丽','女','1976-01-23',95033),
# 								 ('101','李军','男','1976-02-20',95033)])
# 	# 提交到数据库执行
# 	db.commit()
# 	print('ok')
#
#
# except pymysql.err.Error as e:
# # except Exception as e:
# 	# 如果发生错误则回滚
# 	db.rollback()
# 	print(e)
# sql1='''select * from student where ssex=(%s)
# '''
# cursor.execute(sql1,'男')
# rows=cursor.fetchall()
# for i in rows:
# 	print(i)
# # 关闭数据库连接
# db.close()
# sql1 = """SELECT * FROM test_hsry_data WHERE `code`  between '4260000' and '4260010';
# """



#封装mysql  mysql_info 连接池配置信息
mysql_info={"host":"112.74.192.99",
"user":"root",
"password":"Ld123456BJ",
"db":'test',
"port":3306,
"charset":"utf8"}



class MysqlUtil():
	'''
	mysql 数据库相关操作
	连接数据库信息：mysql_info
	创建游标：mysql_execute
	查询某个字段对应的字符串：mysql_getstring
	查询一组数据：mysql_getrows
	关闭 mysql 连接：mysql_close
	'''
	def __init__(self):
		self.db_info = mysql_info
		u'''连接池方式'''
		self.conn = MysqlUtil.__getConnect(self.db_info)
	@staticmethod
	def __getConnect(db_info):
# 静态方法：@staticmethod
# 不能访问实例属性！！！   参数不能传入self！！！
# 与类相关但是不依赖类与实例的方法！！
		'''静态方法，从连接池中取出连接'''
		try:
			conn = pymysql.connect(host=db_info['host'],
			port=db_info['port'],
			user=db_info['user'],
			passwd=db_info['password'],
			db=db_info['db'],
			charset=db_info['charset'])
			return conn            #打开数据库操作
		except Exception  as a:
			Log().debug("数据库连接异常：%s"%a)
			# print("数据库连接异常：%s"%a)
	def mysql_execute(self, sql):
		'''执行 sql 语句'''
		cur = self.conn.cursor()
		try:
			cur.execute(sql)
		except Exception as a:
			self.conn.rollback() # sql 执行异常后回滚
			Log().debug("执行 SQL 语句出现异常：%s"%a)
			# print("执行 SQL 语句出现异常：%s"%a)
		else:
			cur.close()
			self.conn.commit() # sql 无异常时提交
	def mysql_getrows(self,sql,number=None):
		''' 返回查询结果'''
		cur = self.conn.cursor()
		try:
			cur.execute(sql)
		except Exception as a:
			Log().debug("查询结果错误：%s" % a)
			# print("查询结果错误：%s" % a)
		if number == 'one':
			row = cur.fetchone()
			return row
		elif number == 'more':
			rows = cur.fetchall()
			cur.close()
			return rows
		else:
			pass
			cur.close()
	def mysql_getstring(self,sql):
		'''查询某个字段的对应值'''
		rows = self.mysql_getrows(sql)
		if rows != None:
			for row in rows:
				print(row)
				print(row[0])
				for i in row:
					
					print(i)
		
	def mysql_close(self):
		''' 关闭 close mysql'''
	
		try:
			self.conn.close()
		except Exception as a:
			Log().debug("数据库关闭异常：%s" %a)
			# print("数据库关闭时异常：%s" % a)



if __name__ == "__main__":
	mysql = MysqlUtil()
	# sql = "SELECT * FROM test_hsry_data WHERE `code`  between '4260000' and '4260010'"
	sql1=  "select * from student where sno='105'"
	sql2="update"
	mysql.mysql_execute(sql1)
	print(mysql.mysql_getrows(sql1,'one'))
	mysql.mysql_getstring(sql1)
	mysql.mysql_close()