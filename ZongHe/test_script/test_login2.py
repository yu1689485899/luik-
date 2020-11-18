"""
测试登录功能
"""

import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def fail_data(request):  # 固定写法
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):  # 固定写法
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data, ur1, baserequests, db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(ur1, baserequests, setup_data['casedata'])
    yield
    # 删除注册用户


def test_login(register, fail_data, ur1, baserequests):
    # 登录
    # 检查登录的结果
    r = Member.login(ur1, baserequests, fail_data['casedata'])
    assert r.json()['msg'] == fail_data['expect']['msg']
