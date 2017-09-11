#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用list和tuple

#list:
classmates = ['Michael', 'Bob', 'Tracy']

print(classmates[0]) #'Michael'
print(classmates[-1]) #'Tracy'

classmates.append('Adam')

classmates.insert(1, 'Jack')

classmates.pop()

classmates[1] = 'Sarah'

L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']

#tuple:
#tuple和list非常类似，但是tuple一旦初始化就不能修改

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
