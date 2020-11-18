"""
登录的测试脚本(pytest)
"""

import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_success.yaml"))
def success_data(request):  # 固定写法
    return request.param


# 注册成功
def test_register_pass(success_data, ur1, baserequests):
    print(f"测试数据为：{success_data['casedata']}")
    print(f"预期结果为：{success_data['expect']}")

    # 初始化环境
    # DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(ur1, baserequests, success_data['casedata'])
    assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['status'] == success_data['expect']['status']
    assert r.json()['code'] == success_data['expect']['code']


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_success.yaml"))
def success_data1(request):  # 固定写法
    return request.param


# 登录成功
def test_login_pass(success_data1, ur1, db, baserequests):
    print(f"测试数据为：{success_data1['casedata']}")
    print(f"预期结果为：{success_data1['expect']}")
    phone = success_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(ur1, baserequests, success_data1['casedata'])
    assert r.json()['msg'] == success_data1['expect']['msg']
    assert r.json()['status'] == success_data1['expect']['status']
    assert r.json()['code'] == success_data1['expect']['code']
    # # 清理环境，根据手机号删除注册用户
    # DbOp.deleteUser(db, phone)


@pytest.fixture(params=DataRead.readyaml("ZongHe\data_case\login_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param


# 登录失败
def test_login_fail(fail_data, ur1, baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    # 发送请求
    r = Member.register(ur1, baserequests, fail_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['code'] == fail_data['expect']['code']







