#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用 r'' 表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

#用'''...'''格式表示多行内容
print('''line1
line2
line3''')

#还可以结合使用
print(r'''line\1
line\2
line\3''')

#布尔值只有 Ture\False 注意大小写
#布尔值可以用 and\or\not 运算

#空值用 None 表示，None不等于0，而是一个特殊空值

#同一个变量可以反复赋值，而且可以是不同类型的变量
#这种变量本身类型不固定的语言称之为动态语言

#Python中根本没有常量，仅仅是用全部大写的变量名表示常量

#Python中的两种除法
print(9/3) #3.0
print(10//3) #3 称为地板除，仅保留整数部分
