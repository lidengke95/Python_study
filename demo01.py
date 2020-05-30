
'''
print("hello world！world！")
print("hello world! ")

print("------------------------------")

print(999*123456789)


print("------------------------------")


type(2.333)
print(type(2.333))


Valuetype =type(2333)
print(Valuetype)

print("------------------------------")

print(1==1)

print("------------------------------")

'''


#元组
'''
yuanzu = (2,3,5,"哈哈哈哈",False,None,2.333,"xixi")
print(yuanzu)
'''

# 统计值数量
'''
print(count(yuanzu))
'''

#下标（索引）
# print(type(yuanzu[6])) 





'''
X = 1
Y = 2
print(X) 
print(type(Y))
'''


# x = 'wahha'
# Y = "娃哈哈"
# print(type(x))
# print(type(Y))

print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")

# 数组
# shuzu = [2,3,5,"哈哈哈哈",False,None,2.333,2333,2333,"xixi","xixi"]
'''
shuzu.remove("xixi")
shuzu.remove(2333)

print(shuzu)
'''

'''
shuzu = [5,2,"haha"]
shuzu.pop(1)
print(shuzu)
'''

'''
shuzu = [2,3,5,"哈哈哈哈",False,None,2.333,2333,2333,"xixi","xixi"]
y = tuple(yuanzu)
print(y)
print(type(y))
'''


'''
xx = input("请输入你的年龄：")
print(xx)
print(int(xx)+6)

'''


'''

name = input("请输入你的名字：")
age = input("请输入你的年龄：")
ai = input("请输入你的爱好：")

print("你好!{name1},我今年{age1},我的爱好是{aihao}。\
    我今年{age1},我的爱好是{aihao}".format(name1=name,age1=age,aihao=ai))


'''

'''
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))

if a == b:
    print("第一个数字比第二个数字大！")
elif a == b:
    print("第一个数字和第二个数字一样大！")
else:
    print("第一个数字比第二个数字小！")

'''

'''
输入一个数字，如果大于60就放到hlist数组中，如果小于60就放到lowlist中。
'''

'''
a = range(20)
print(a)
'''






'''
# 生成20个值得数组
a = list(range(20))
print(a)
'''


'''
# 生成20个值得元组
a = tuple(range(20))
print(a)

'''

'''
hlist = "你好，现在是北京时间0：30,你会成功的！"
for i in hlist:
    print(i)
'''


'''
for i in range(100):
    print(i)
'''
'''
hlist = [1,2,3,4,5,6]
highnum = []
lownum = []
for i in hlist:
    if i > 4:
        highnum.append(i)   
    else:
        lownum.append(i)
print('大于4的数字有{}个 ,小于4的数字有{}个'.format(len(highnum),len(lownum)))
'''


'''
hlist = [1,2,3,4,5,6]
highnum = []
lownum = []
for i in hlist:
    if i > 4:
        highnum.append(i)
    else:
        lownum.append(i)
print("大于4的数字有{}个，小于4的数字有{}个".format(len(highnum),len(lownum)))
'''
'''

for i in range(1,10):
    for j in range(1,i+1):   #1是遍历起始值；i+1是因为,i索取为i的前一位值（即成了i-1），故此i要+1
        print('{}X{}={}'.format(i,j,i*j),end='  ')
    print("")

'''

'''
for i in range(1,4):
    for j in range(1,i+1):
        print('{}X{}={}'.format(i,j,i*j))
print("---------------------------------------------------")
for i in range(1,4):
    for j in range(i+1):
        print('{}X{}={}'.format(i,j,i*j))
print("---------------------------------------------------")
for i in range(1,4):
    for j in range(1,i+1):   #1是遍历起始值；i+1是因为,i索取为i的前一位值（即i-1），故此i要+1
        print('{}X{}={}'.format(i,j,i*j))
'''



a = [1,2,3]

print(a[0])
