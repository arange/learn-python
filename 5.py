#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#条件判断
#......
#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#使用dict和set
#dict:
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d) #False
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)

d.pop('Bob')
#set:
#在set中，没有重复的key
s = set([1, 2, 3])
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
s.remove(4)

#两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)
