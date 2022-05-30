# 三目运算符
# True_statements if expression else False_statements
# 平时：
# a = 1
# b = 2
# if a + b > 3:
#     print(a + b)
# else:
#     print(b - a)

# 三目运算符：   当判断返回为真时，执行前面的表达式，返回为假时执行后面的表达式
a = 1
b = 3
print(a + b if a + b > 3 else b - a)   #三目运算符  和c语言里面有很大的差别

