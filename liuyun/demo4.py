# while：

a = 1
while a < 10: # 满足条件，就继续执行while里面的内容，不满足，就不会执行了
    print(a)
    a = a + 1


# 死循环：一直重复不断的执行，永远都不会退出，强制退出:ctrl+c
# a = 1
# while a < 10: # 满足条件，就继续执行while里面的内容，不满足，就不会执行了
#     print(a)

#
# 1. a=1, 1, a=2(1+1)
# 2. a=2, 2, a=3(2+1)
# 3. a=3, 3, a=4(3+1)
#....
# 8. a=8, 8, a=8(7+1)
# 9. a=9, 9, a=10(8+1)



'''
作业：输入账号和密码，去判断db中是否存在该账号，如果已存在，就修改该账号的密码，如果不存在，就新增一个字典
db = [{"username":"chenke", "password":"123456"}]
输入一个账号为chenke，那就需要把password改成输入的密码
输入的账号是zqc，那就新增一个字典
db = [{"username":"chenke", "password":"123456"}, {"username":"zqc", "password":"123456"}]

变量
db = [{"username":"chenke", "password":"123456"}]
输入
u = input("请输入账号：")
p = input('请输入密码：')

循环判断db中有没有账号zqc的账号

如果有：就去修改zqc的账号

如果没有：就要去新增zqc的账号和密码
'''





