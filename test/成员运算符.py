#成员运算符
#in与not in 是python独有的运算符（全都是小写字母），用于判断对象是否是某个集合的元素之一。  返回值为：布尔类型的True 或 Flase

# in      判断某个值是否在指定序列中，在则返回Ture
# not in  判断某个值是否在指定序列中，在则返回Ture

name = "xiaoming"
class_li = ["xiaoming", "xiaohong", "小宇"]
# 判断 xiaoming 在 class_li 中则返回ture
if name in class_li:
    print("在")
else:
    print("不在")

