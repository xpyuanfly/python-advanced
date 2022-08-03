# 第一周 迭代器
迭代器 iterator：iter(),next()
生成器 [ x for x in iteratable]
递归recursive: define cur 和 next的关系，define break final point
map,reduce,filter: 
map(lambda x: x, iteratable)
reduce(lambda x,y: x+y,iteratable)
filter(lambda x: True or False, iteratable)
自定义iterator：yield关键字：暂停运行过程输出当前结果并保留状态，状态包括上次终止的位置和终止时的数值。
## 第二周 Stack
stack：FILO（First In, Last Out）
自定义stack，list首是stack底，list尾是stack首，pop()是弹list尾，push=》append压list尾
单调栈：解决直方图面积
基本计算器：栈的基本用法
最小栈：双栈封装
## 第三周 quene
quene：FILO（First In, First Out）
自定义quene
heap堆结构的定义和用法，大根堆、小根堆
## 第四周 hashtable
基本用法 wordcount
2 妙用补数查两数之和
3 查表在不在里面基本用法
36 数独，难度在如何切割（郭源方法的j、i互换很妙）
49 （1）排序的元组作为key，消除字串有序的干扰（都整平），（2）list的扩展方式：extend，或者[] + [] 