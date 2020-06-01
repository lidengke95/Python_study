# 判断

# a = 123 # 赋值语句， = 等号左边是变量 右边是值


# if：判断
# 缩进
# b = 19
# if b == 18: # 条件语句
#     print("成年人")
#     print("后果自负")
# else:
#     print("未成年人")
#     print("受保护")



# f = d in e # d in e == 找打了就True/False
# c = "快儿童乐节"
# d = "儿童节"
# e = ["快乐儿童节", "儿童节"]
# if d in e:  # d不在e中，print 23 / 在e中就print25
#     print("d在c中找到了")
# else:
#     print("不在")


# g = "哥哥"
# h = "妹妹"
# j = "哥哥"
# if g is h:
#     print("g是h本身")
#     if 1==2:
#         print("123")
#     else:
#         print("456")
# else:
#     print("g不是h本身")

# else:可选的
# if 2==2:
#     print("123")


# == 是判断两个变量的值是否相等
# is 是判断两个变量的值和内存地址是否相等



a = 1
b = 2
c = 3

# if c > b and b > a:
#     print("c>b 并且b>a")
# else:
#     print("错了")

if c > b or a > b:
    print("c>b 或者a>b")
else:
    print("错了")
    