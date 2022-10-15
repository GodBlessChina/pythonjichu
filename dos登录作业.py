import hashlib
import pwinput  # 密码输入包  pip3 install pwinput

# 作业： 只需要删除 def login():里面的代码，重新敲出来，10分钟

"""
dos登录
作者: 周扒皮
时间: 2022年10月5日
"""

# 定义一套账号密码
account_pwds = [{"account":"zhoubapi", "pwd":"e10adc3949ba59abbe56e057f20f883e"},# 123456
                {"account":"wangmazi", "pwd":"fcea920f7412b5da7be0cf42b8c93759"}, # 1234567
                {"account":"jack", "pwd":"25d55ad283aa400af464c76d713c07ad"}] # 12345678


def my_md5(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def login():
    """
    这个函数是用来登录我们自己的系统的。
    1 提示用户输入账号
    2 提示用户输入密码
    3 判断账号密码是否正确
    4 结束。
    :return:  None
    """
    account = input("请输入账号:")
    # pwd = input("请输入密码:") # toDO 这里不能让别人看见密码
    pwd = pwinput.pwinput("请输入密码:", "*")
    pwd = my_md5(pwd) # 加密密码
    print(f"你输入的账号密码是:{account} | {pwd}")  # 输入的账号和密码
    # 判断账号密码是否正确
    # 迭代 account_pwds
    print("系统中已经存在的账号密码是：")
    for account_pwd in account_pwds:
        system_account = account_pwd['account']  # 系统账号
        system_pwd = account_pwd['pwd']         # 系统密码
        print("系统中的账号是:",system_account)
        print("系统中的密码是:", system_pwd)
        # 对比用户输入的账号和密码，看输入的是否正确
        # if system_account.__eq__(account) and system_pwd.encode(pwd):
        #     print('登录成功')
        print(f'输入的账号是:{account} 系统账号是:{system_account}')
        print(f'输入的密码是:{pwd} 系统密码是:{system_pwd}')
        if system_account.__eq__(account):
            if not system_pwd.__eq__(pwd):
                print("账号正确，但是密码不正确，登录失败")
                return
            else:
                print('登录成功!!!') #TODO 打印成彩色的
                return
        print('=======================================')
    # TODO 代码如果能走到这里，说明
    print("账号不存在，登录失败")

# 调用login函数
login()
# if __name__ == '__main__':
#     login()

