# coding:utf-8
import unittest
import HTMLTestReportCN
import HTMLTestRunner_cn
import os
from common.smtp_Email import send_email
# 待执行用例的路径
case_path = os.path.join(os.getcwd(),'case')
# 报告存放目录
report_path=os.path.join(os.getcwd(),'report')
print(report_path)
def all_case():

    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
  
    print(discover)
    return discover
if __name__ == "__main__":
# html报告文件路径-决对路径
    report_abspath = os.path.join(report_path, "result.html")
    fp=open(report_abspath,'wb')
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
    title=u'这是我的自动化测试报告',
    description=u'用例执行情况：')
    send_email()        # 生成报告自动发送报告文件
    # run 所有用例
    runner.run(all_case())
    fp.close()
#

   


