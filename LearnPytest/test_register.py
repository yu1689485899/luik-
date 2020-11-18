"""
pytest命名规则:
1、测试文件以test_开头或结尾
2、测试类以Test开头
3、测试方法/函数以test_开头
"""
import requests


def register(data):
    # url = "http://jy001:8081/futureloan/mvc/api/member/register"
    url2 = "http://jy001:8081/futureloan/mvc/api/member/login"
    r = requests.post(url2, data=data)
    return r


# 手机号码格式不正确
# def test_register_001():
#     # 测试数据
#     data = {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"}
#     # 预期结果
#     expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']


# def test_register_002():
#     # 测试数据
#     data = {"pwd": "123456abc", "regname": "aaa"}
#     # 预期结果 otf0f  0tf0
#     expect = {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']


# def test_register_003():
#     # 测试数据
#     data = {"mobilephone": "137", "pwd": "123456abc", "regname": "aaa"}
#     # 预期结果
#     expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']


# def test_register_004():
#     # 测试数据
#     data = {"mobilephone": "1371234111a", "pwd": "123456abc", "regname": "aaa"}
#     # 预期结果
#     expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']


# def test_register_004():
#     # 测试数据
#     data = {"mobilephone": "13712341111", "pwd": "123456abc", "regname": "aaa"}
#     # 预期结果
#     expect = {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']


# def test_register_005():
#     # 测试数据
#     data = {"mobilephone": "13712341111", "pwd": "12", "regname": "aaa"}
#     # 预期结果
#     expect = {"status": "0", "code": "20108", "data": None, "msg": "密码长度必须为6~18"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']

# def test_register_006():
#     # 测试数据
#     data = {"mobilephone": "15212345689", "pwd": "1234567", "regname": "aaa"}
#     # 预期结果
#     expect = {"status": 1, "code": "10001", "data": None, "msg": "注册成功"}
#     # 测试步骤
#     real = register(data)
#     # 检查结果
#     assert real.json()['msg'] == expect['msg']
#     assert real.json()['code'] == expect['code']


def test_register_007():
    # 测试数据
    data = {"mobilephone": "15212345689", "pwd": "1234567", "regname": "aaa"}
    # 预期结果
    expect = {"status": 1, "code": "10001", "data": None, "msg": "登录成功"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']

