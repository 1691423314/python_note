# #字符串
# #可以用单引号或者双引号来创建单行字符串，使用三引号创建多行字符串。
# s1="hello"
# print(s1)
# s2='he' \
#    'llo'
# print(s2)
# #三引号可以保留在里面进行的操作，而单引号，和双引号则不会
# s3='''he''l""lo'''
# print(s3)

#字符串的存储
#字符串在内存中每一个字符都是单独存储的，也就是字符串数组
#由于字符串是序列数据结构，所以我们可以通过下标将字符串中某个字符串中的某个字母取出来
#下标也称索引，从开始
#
# name="lizhenhui"
# print(name[-1])#向后从前取
# print(name[10])   #IndexError: string index out of range  索引错误，超过了范围，越界访问
#注意：字符串是不可改变类型，即使取出来也不能进行改变

#字符串的切片（重点）
#切片是左闭右开的
# 函数原型：slice(start,stop[,step])   start:起始位置    stop：结束位置     step:步长（是可选参数）
# name="hello world"
# print(name[6:10])#切片是左闭右开的
# print(name[6:11])
# print(name[6:]) #不写结束位置默认到结尾
# print(name[6::2])#步长为2则一次走两步，取一个
# print(name[6::4])

# #字符串类型转换
# #将int类型转换为字符串  str方法
# # print(str(1)) #将整数转换为字符串
#
# print('1'+'2')   #字符串用+做拼接
#
# #和c语言一样的%占位
# # str.format()格式
# name="kaeufbaf"
# age=20
# print("{}年龄为：{}".format(age,name))
# # f''模式
# print(f"{name}年龄为{age}")
# #下面这两种方法的优点：不用规定数据的类型 ，前后的位置也可以交换

#字符串方法：
#find方法:
#字符串查询
# s1="hello python"
# print(s1.find("e")) #返回最小索引
# print(s1.find('o'))
# print(s1.find("x"))#没有返回-1

#index   字符串索引  当找不到会报错，而不是返回1，
#index   和find  的作用一样，但是区别在于
#S.index查询不存在的子串时，会报错，而S.find找不到时返回-1

# #字符串替换
# s2="hello world"
# # s2.replace("旧字符串要被替换的次数","替换的字符串",替换次数)
# print(s2.replace("world","lizhenhui",1))
# print(s2)  #源字符串没有被改变，以为替换是，是临时拷贝了一份进行了替换，并不会该=改变原有的值。

# #split  字符串分割
# s3="hello everybody omgad"
# #以空格将三个单纯进行拆分为列表元素
# print(s3.split(" ")) #以空格字符串进行分割，那空格字符串消失   里面填啥就以啥进行分割，字符，符号都行，  返回列表
# print(type(s3.split(" ")))
# print(s3)   #和前面的一样都是临时拷贝并不改变，其源值

# s4="hello everybody omgad"
# print(s4.startswith("hell"))  #判断字符串是否以，某字符串开始，   返回为一个布尔值
# print(s4.endswith("ad"))  #判断字符串是否以，某字符串结束，  同样返回布尔值

# #s.upper()
# s5="n"
# s5_1='N'
# print(s5.upper())  #将小写转换为大写
#
# #s.lower()将大写转换为小写
# print(s5_1.lower())
# print(s5.lower().upper())  #链式调用



# #strip()  方法去掉字符串中的空格 只能去除  开头和结尾的空格
# s7="   李   振   辉   "
# print(s7.strip())
#
# #那么这么去掉，中间的空格呢？
# print(s7.replace(" ",""))  #将有空格的字符串，替换为无空格的字符串    会删掉所以的空格   replace：英语单词，替换，更换的意思


# s8="你好呀"
#
# #实现：“你  好”  向其中加入空格
# #字符串序列  字符串时一个序列，考研一个个取出它的元素————>是可迭代的（iterable）  也就是，考研一个个取出的
# print(" ".join(s8))  #join 传参需要传入一个可迭代的对象
# #实现了，每一个中间都加上了，空格

# li =["你好","世界"]  #列表也是可迭代的
# print(li)
# print(" ".join(li))




