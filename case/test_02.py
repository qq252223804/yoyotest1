# import requests
# import unittest
#
#
# class RunMain(unittest.TestCase):
#     # def __init__(self, url, method, data=None):  # 构造函数 就不用下面每次实例化了
#     #     self.res = self.method_main(url, method, data)
#
#     def GET(self, url, data):
#         # url=ReadExcel(0,1,2)
#         # data=ReadExcel(0,1,3)
#         # url1 = url + '?' + data
#         # print url1,data
#         # req = urllib2.Request(url1)
#         # response = urllib2.urlopen(req)
#         # page=response.read()                  #  不采取urllib2进行传参数！！！
#         # # print response.getcode,response.msg
#         # # print(page)
#         # return page
#
#         html = requests.get(url, data)
#         # print(html.text)
#         # print(html.status_code)
#         return html.text
#
#     def POST(self, url, data, headers=None):
#         # url=ReadExcel(0,3,2)
#         # data=ReadExcel(0,3,3)
#         # print(data) ,type(data)
#
#         # data1 = data.encode('utf-8')  # 将 Unicode 转换成 str
#         # # print data,type(data1)
#         # datas = eval(data1)  # 将str 转换成 dict
#         # # print(datas),type(datas)
#
#         html = requests.post(url, data=data, headers=headers)
#         # print(html.status_code)
#         return html.text
#
#     def method_main(self, url, method, data=None, headers=None):
#         respose = None
#         if method == 'GET':
#             respose = self.GET(url, data)
#         else:
#             respose = self.POST(url, data, headers)
#         return respose
#     def test_01(self):
#         url = 'http://www.imooc.com'
#         data = {
#             "cart": "11"
#         }
#
#         respose = RunMain().method_main(url, 'GET', data)
#         print(respose)
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#     run = RunMain()  # 实例化
#     url = 'http://www.imooc.com'
#     data = {
#         "cart": "11"
#     }
#
#     respose = run.method_main(url, 'GET', data)
#     # print (json.dumps(respose, indent=2, sort_keys=True))
#
#     # print (type(respose))
#
#     print(respose)
#
import unittest
import requests
import json


class Test_Kuaidi2(unittest.TestCase):
    def setUp(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.s = requests.session()
    
    def test_yunda(self):
        '''快递单号查询'''
        kd = 'yunda'
        danhao = '1202247993797'
        
        # 这里对 url 的单号参数了
        self.url = "http://www.kuaidi100.com/query?type=%s&postid=%s&id=1&valicode=&temp=0.6220324459573068l" % (
            kd, danhao)
        print(self.url)
        r = self.s.get(self.url, headers=self.headers, verify=False)  # 如果你将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证
        result = r.json()
        # print(result)
        print(json.dumps(result, indent=2, sort_keys=True,
                         ensure_ascii=False))  # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：
        # print(result['message'])

        self.assertIn('ok', result['message'], msg='a不在b中')
        self.assertTrue(result['status'] == '200', msg='状态不对')
        self.assertEqual('1202247993797', result['nu'], msg='')  #判断是否相等,不相等抛出msg  # 判断是否相等,不相等抛出msg


if __name__ == "__main__":
    unittest.main()