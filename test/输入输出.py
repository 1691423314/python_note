# 输出  %占位符
# Ctrl+鼠标左键 进入说明文档
# sep:插入在两个值之间，默认为" " 空


# print函数的原型为：
# def print(object(s),sep=" ",end="\n",file=sys.stdout,flush=False)
#
# 上面的函数原型给出了一些参数的默认值，在日常的使用过程中，除了第一个参数，后面的参数都是可选的，对于可选参数将使用其默认值。
# 这些参数的具体作用如下：
# object(s)参数表示各种对象，例如元组，字典，列表，字符串等，当print函数中要输出多个对象时需要使用逗号","分隔；
# sep参数决定用什么符号来分隔这些对象，默认使用空格；
# end参数决定输出结尾用什么字符来结束，默认使用换行符；
# file参数表示输出的目标对象，默认参数为sys.stdout，也可以是文件或其它具有写属性的对象；
# flush参数取值为布尔类型，该参数决定了是否立刻将输出语句输出到目标对象，True表示立刻输出到目标对象，False表示先写入缓存。


# #常用参数
# sep:分隔符符号，在值之间插入的字符串，默认为空格
# end:字符串追加在最后一个值之后，默认为换行符
# 如果，设置end'' ,则可以不换行，让print在一行内连续打印。

#
# Name = "李振辉"
# classPor = '清华大学'
# age = 18
# print('我的名字是:%s 来自【%s】 今年%d岁了' % (Name, classPor, age))
# #  \n 换行
# print('nihao\n  wohenhap ')
#
# name2 = input("请输入你的姓名：")
# print("%s" % (name2))


# #输入
# #input
# #input(*args, **kwargs):  函数的定义
# # num=input("提示信息")
# age = input("输入信息")
# print(type(age))
# # input 不管输入的是什么，其都是字符串类型  str
# # input 会阻塞
# print('欢迎来到我的世界')
# input("你是谁") #在这里会发送阻塞  一直在这里等待，用户输入  输入完了才会进行下一步
# print("你好我是我")


# age = input("请输入年龄")  #不管输入什么input都是字符串类型
# if int(age) >= 18:  #因为输入的年龄age是字符串类型，而18是整型，所以两个之间不能比较会报错，所以这里要用到强制类型转换。
#     print("你好啊靓仔")
# else:
#     print("小朋友你好")

#短路（懒惰）机制    非0为真 
print(10 and 20)  #20
print(10 or 20)  #10


#这里可以类比，离散数学里面
# 或 运算  只要有真为真， 所以前面为真后面的就不在执行了。
# 与 运算  全真为真，   所以要判断完每一个
print(False and False) #False
print(True or False) #True