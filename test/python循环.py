# 循环分类
# while  语法结构
# while 条件表达式
#  代码指令
#  语法特点
# 1.有初始值
# 2.条件表达式
# 3.变量【循环体内计数变量】的自增自减，否则会造成死循环
# 使用条件：循环的次数不确定，是依靠循环条件来 结束
# 目的：为了将相似或者相同的代码来操作变得简洁，使代码可以重复利用
# #for 循环

# for 临时变量 in 字符串 ，列表等：
#     执行代码块
#遍历操作依次的取集合容器中的每个值

# tages ='helllo'  #字符串类型本身就是一个字符类型的集合
# for item in tages:
#     print(item)
#     pass  #空语句什么也不执行

# range 函数 可以动态的生成一个数据集合列表   range：区域

#range()


# while 循环
# 基本结构

# while 判断条件(condition)：
#     执行语句(statements)……


# index=0
# while index<=100:  #注意这里有冒号
#     print(index)
#     index+=1  #python里面没有自加运算 不能使用 ++
#     #pass     #pass可以去掉
#

# 打印9*9乘法表
row = 1  # 行

j = 1
while row <= 9:
    col = 1  # 列
    while col <= row:
        print("%d*%d=%d" % (row, col, row * col), end="  ")  # print打印时默认会换行，可以在后面加上控制语句，让其不换行
        col += 1
        pass
    print("\n")
    row += 1
    pass
