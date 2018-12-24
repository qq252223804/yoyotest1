# coding:utf-8
import xlrd


class excel:
	def __init__(self):
		self.test_data_path = 'F:\\testdata.xlsx'

	def open_excel(self, file):
		u'''读取excel文件'''
		try:
			data = xlrd.open_workbook(file)
			return data
		except Exception as e:
			raise e

	def excel_table(self, file, sheetName):
		u'''装载list'''
		data = self.open_excel(file)
		# 通过工作表名称，获取到一个工作表
		table = data.sheet_by_name(sheetName)
		# 获取行数
		Trows = table.nrows
		# 获取 第一行数据
		Tcolnames = table.row_values(0)
		lister = []

		for rownumber in range(1, Trows):   #遍历所有行
			row = table.row_values(rownumber)  # 所有行的数据
			print(row)
			if row:
				app = {}
				for i in range(len(Tcolnames)):
					app[Tcolnames[i]] = row[i]
				lister.append(app)
				print(lister)
		return lister

	def get_list(self, sheetname):
		try:
			data_list = self.excel_table(self.test_data_path, sheetname)
			assert len(data_list) >= 0, u'excel标签页:' + sheetname + u'为空'
			return data_list
		except Exception as e:
			raise e

a=excel.get_list(sheetname=1)
