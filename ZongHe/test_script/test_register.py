"""
注册的测试脚本(pytest)
"""

import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


# def register(data):
#     url1 = "http://jy001:8081/futureloan/mvc/api/member/register"
#     r = requests.post(url1, data=data)
#     return r


# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param


# @pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_cf.yaml"))
# def cf_data(request):  # 固定写法
#     return request.param

# 注册失败
def test_register_fail(fail_data, ur1, baserequests,db):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    # 发送请求
    DbOp.deleteUser(db)
    r = Member.register(ur1, baserequests, fail_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['code'] == fail_data['expect']['code']


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_success.yaml"))
def success_data(request):  # 固定写法
    return request.param


# 注册成功
def test_register_pass(success_data, ur1, db, baserequests):
    print(f"测试数据为：{success_data['casedata']}")
    print(f"预期结果为：{success_data['expect']}")
    phone = success_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(ur1, baserequests, success_data['casedata'])
    assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['status'] == success_data['expect']['status']
    assert r.json()['code'] == success_data['expect']['code']
    # 2.检查实际有没有被注册(1.数据库;2.获取用户列表;3.用注册的用户登录)
    r = Member.getList(ur1, baserequests)
    print(r.text)
    assert phone in r.text
    # 清理环境，根据手机号删除注册用户
    DbOp.deleteUser(db, phone)


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_cf.yaml"))
def cf_data(request):  # 固定写法
    return request.param


# 重复注册
def test_register_cf(cf_data, ur1, db, baserequests):
    print(f"测试数据为：{cf_data['casedata']}")
    print(f"预期结果为：{cf_data['expect']}")
    phone = cf_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(ur1, baserequests, cf_data['casedata'])
    assert r.json()['msg'] == cf_data['expect']['msg']
    assert r.json()['status'] == cf_data['expect']['status']
    assert r.json()['code'] == cf_data['expect']['code']
    r1 = Member.register(ur1, baserequests, cf_data['casedata'])
    assert r1.json()['msg'] == '手机号码已被注册'
    assert r.json()['code'] == '10001'
