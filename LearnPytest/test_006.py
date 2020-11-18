import pytest
import requests


def register(data):
    url1 = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url1, data=data)
    return r


@pytest.fixture(params=[
    {"data": {"mobilephone": "15212345624", "pwd": "1234567", "regname": "aaa"},
     "expect": {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}},
    {"data": {"mobilephone": "1521", "pwd": "1234567", "regname": "aaa"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
    {"data": {"mobilephone": "", "pwd": "1234567", "regname": "aaa"},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}},
    {"data": {"mobilephone": "19876543210", "pwd": "123", "regname": "aaa"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    {"data": {"mobilephone": "aaa", "pwd": "1234567", "regname": "aaa"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}])
def data1(request):
    return request.param


def test_login(data1):
    r = register(data1['data'])
    assert r.json()['code'] == data1['expect']['code']
    # assert r.json()['msg'] == data1['expect']['msg']
    print(f"使用手机号{data1['data']['mobilephone']}注册显示{data1['expect']['msg']}")
