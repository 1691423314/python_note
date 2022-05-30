# 在Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。
# bytes数据类型在所有的操作和使用甚至内置方法上和字符串数据类型基本一样，也是不可变的序列对象。
# Python3中，bytes通常用于网络数据传输、二进制图片和文件的保存等等。
# 爬虫爬到的数据一般为字节类型

#字节码

#bt_1 = b"hello"  # 字节类型的字符串   bt 为 bytes的简称
# print(type(bt_1))  #bytes类型   <class 'bytes'>

# 创建字节类型   bytes(string, encoding[, errors])   如果用该方法，把字符串转换为，字节类型，需要指定它的类型
# gbk:中国码  utf-8:万国码  适用的环境更广
# bt_2 = bytes("hello", encoding="utf-8")
# print(bt_2)
# print(type(bt_2))

#重点  #字节与字符串之间的转换
#
#字节转换为字符串
# bt_3=b"hello world"
# print(type(bt_3))
#
# #将bt_1  转换为str类型
# #字节转换为 我们能读懂的字符串类型 --->解码
# print(bt_3.decode())  #decode  解码的意思
# print(type(bt_3.decode()))   #转换成了字符串类型

# 次要 #将字符串转换为字节  --->编码
# s_2="hello world"
# bt_4=s_2.encode()   #en前缀有使动的意思， 使编码
# print(bt_4)
# print(bt_4[0])   #ascii  转换为了ASCII码

