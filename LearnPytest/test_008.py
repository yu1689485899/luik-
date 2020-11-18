"""
取现接口
"""

from unittest import mock

import requests


class JinRong:
    def chongzhi(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge", data=data).json()
        return r

    def quxian(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw", data=data).json()
        return r


class TestJinRong:
    def test_quxian(self):
        jinrong = JinRong()
        c = {"mobilephone": 18012345678, "amount": 1000}
        r = jinrong.chongzhi(c)
        assert r['msg'] == "充值成功"
        assert r['status'] == 1
        assert r['code'] == str(10001)
        jinrong.quxian = mock.Mock(return_value={'status': 1, 'code': '10001', 'data': None, 'msg': '取现成功'})
        data = {"mobilephone": 18012345678, "amount": 50}
        r1 = jinrong.quxian(data)
        assert r1['msg'] == "取现成功"
        assert r1['status'] == 1
        assert r1['code'] == '10001'
        print(r)
        print(r1)
