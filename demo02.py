

'''
#数组（列表）
list1 = [0,2,5,8,6,4] 
list2 = ["ahhh",2333,"啊哈哈哈",85954]

print(list1[1:3])
print(list2[1:3])
'''




#方法的封装
'''
def jiafa(*num):
    print(num)
    nums = 0
    for i in num:
        nums = nums + i
    print(nums) #教学

jiafa(1,5,4,6,8,99,12,1)

'''


'''
#一般工作中的操作
def jiafa(*num): #(*num):可变参数，可以传入任意多个数字，计算和
    nums = 0
    for i in num:
        nums = nums + i
    return nums #返回nums

xx = jiafa(1,5,4,6,8,99,12,1)
print(xx)

'''

'''
#方法封装的结构：
def 方法的定义(方法的传递):
    代码逻辑
    返回代码结果
'''
'''
# 方法的导入
# 第一种
from 文件 import 方法的定义,方法的定义
方法的定义(参数)  #方法的调用
# 第二种
import 文件
xx = 文件.方法的定义(参数)  #方法的调用
print(xx)
    '''

'''
实现红绿灯的功能(要想到时间、字典、循环、)，每隔一秒，打印一次灯的颜色
'''


'''
import time #5.导入时间，给时间定义

deng = {
    "红灯":30,  #1.灯对应时间，运用字典
    "绿灯":30,
    "黄灯":5
}
while time:  #6.无限循环，Ctrl+c停止while循环
    for i in deng:  #2.灯的循环
        for j in range(deng[i]): #3.灯维持时间
            print("{}距离换灯还有{}秒".format(i,deng[i]-j)) #4.输出格式
            time.sleep(1)  #5.给时间定义，控制闪灯间隔

'''











