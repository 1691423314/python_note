# 我们将c赋值为了整型值256，d也为256，e为257，f为257。但是当把c与d，e与f进行is操作时，
# 却发现两者的结果不同。原因在哪？
# ——这个是由python中的整型对象的缓冲池机制，所决定的。
# 在python中几乎所有的内建对象，都会有自己所特有的对象池机制。
# 1.小整数对象——小整型对象池
# 在实际编程中，数值比较小的整数，比如1,2,29等，可能会非常频繁的出现。而在python中，所有的对象都存在与系统堆上。
# 想想？如果某个小整数出现的次数非常多，那么python将会出现大量的malloc/free操作，这样大大降低了运行效率，
# 而且会造成大量的内存碎片，严重影响Python的整体性能。
# 在python2.5乃至3.3中，将小整数位于[-5,257)之间的数，缓存在小整型对象池中。
# 这也就是为了c is d而e is not f的原因了。
# 2.大整数对象——通用整数对象池
# 由以上知，python把小整型数完全的缓存在了小对象缓存池中了。而那些大整数对象就没有那么好的待遇了！
# python运行环境提供了一块内存空间供大整数轮流使用。通常称为通用整数对象池。这也就是说大整数其实也是有缓存的。
# 该对象池使用链表组织，虽然e和f有着相同的值，但是在链表中确是不同的节点。也就是说e和f根本不是一个对象。
# 至于既然有缓存，为什么e和f还要组织为两个节点，就不大明白了。
# 讲讲我的看法吧：我觉得从语义上来讲e=257和f=257本身就是应当为两个不同的对象(这点和对象赋值不同)。
# 由于整数缓存池的存在，让大家觉得任何整数在缓冲池中都只能存在一个，不能重复。
# 但将e和f在整数缓冲池中组织为一个节点或两个节点没有什么本质区别吧(除了浪费了一点内存)。
# 原博文地址：http://www.zzvips.com/article/166997.html


# “Python中的import语句，可以导入大量的三方库，快速提升我们的工作效率！
import time  # 导入time 库


a = 100000
print(id(a))  # 打印a的内存地址
# del 变量名      就是删除对象
del a  # 删除变量a
time.sleep(10)  # 延迟10秒
a = 100000
print(id(a))
#在py_charm有一个整数缓存区的概念，但是在python官方在并没有这个，知识在，py_charm中支持了，整数缓存区的概念
#python中的整数缓冲区的概念，是刚被删除的整数，不会被真正的立刻删除回收，而是在后台缓存需一段时间，等待下一次
#可能调用
#注意：这些不能是小正实数对象池中的值。

#complex()#复数强制类型转换，不常用
#复数由实数部分和虚数部分构成，可以用a+bj，或者complex（a，b）表示，复数的实部a和虚部b都是浮点类型