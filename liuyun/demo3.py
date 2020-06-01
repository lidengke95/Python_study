# 去判断用户是否登录成功
db = [
        {"username":"张三", "password":"123456"},
        {"username":"李四", "password":"123321"}
    ]

zh = input("请输入账号:")
mm = input("请输入密码:")

for i in db:
    # 先判断账号相等
    if zh == i.get("username"): # 账号相等
        if mm == i.get("password"):
            print("{}登录成功".format(zh))
            break # 终止循环 = 登录成功了，不需要继续往下面循环了
    else:           # 账号不相等
        continue # 跳过本次循环，开始下一次循环



# bug1：版本
# for i in db:
#     print("===============================")
#     print(i)
#     if zh == i.get("username") and mm == i.get("password"):
#         print("输入的账号{}登录成功！".format(zh))
#     else:
#         print("登录失败！")

# for循环嵌套
# for i in db:
#     for a in i :
#         print(a)
#         print(i.get(a))
#         print("===========")

