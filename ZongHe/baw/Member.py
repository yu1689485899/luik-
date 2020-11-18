'''
用户模块的接口(注册、登录、充值、用户列表、取现)
'''


def register(ur1, baserequests, data):
    '''
    发送注册接口
    :param ur1:  http://jy001:8081/,是从环境文件中读取的
    :param BaseRequests: 是BaseRequests的一个实例
    :param data: 注册接口的参数
    :return: 响应信息
    '''
    ur1 = ur1 + "futureloan/mvc/api/member/register"
    r = baserequests.post(ur1, data=data)
    return r


def login(ur1, baserequests, data):
    '''
    发送注册接口
    :param ur1:  http://jy001:8081/,是从环境文件中读取的
    :param BaseRequests: 是BaseRequests的一个实例
    :param data: 注册接口的参数
    :return: 响应信息
    '''
    ur1 = ur1 + "futureloan/mvc/api/member/login"
    r = baserequests.post(ur1, data=data)
    return r


def getList(ur1, baserequests):
    ur1 = ur1 + "futureloan/mvc/api/member/list"
    r = baserequests.get(ur1)
    return r


if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests

    baserequests = BaseRequests()
    canshu = {"mobilephone": 13223123211, "pwd": 132132}
    r = register("http://jy001:8081/", baserequests, canshu)
    print(r.json())

# def login(ur2, BaseRequests, data):
#     ur2 = ur2 + "futureloan/mvc/api/member/login"
#     r = BaseRequests.post(ur2, data=data)
#     return r
#
#
# def getList(ur2,baserequests):
#     ur2 = ur2 + "futureloan/mvc/api/member/list"
#     r = baserequests.get(ur2)
#     return r
#
#
# if __name__ == '__main__':
#     from ZongHe.caw.BaseRequests import BaseRequests
#
#     baserequests = BaseRequests()
#     canshu = {"mobilephone": 13223123211, "pwd": 132132}
#     r = register("http://jy001:8081/", baserequests, canshu)
#     print(r.json())
#
#
