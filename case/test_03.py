import unittest
import requests
import json


class Test_Kuaidi3(unittest.TestCase):
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

        self.assertIn('快递公司参数异常：单号不存在或者已经过期', result['message'], msg='a不在b中')
        self.assertTrue(result['status'] == '201', msg='状态不对')
        self.assertEqual('', result['nu'], msg='查询的单号不正确')  #判断是否相等,不相等抛出msg  # 判断是否相等,不相等抛出msg


if __name__ == "__main__":
    unittest.main()