#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字符串和编码

ASCII编码仅美国使用
Unicode包容所有语言
UTF-8是Unicode的可变长版本

Python3中，字符串以Unicode编码

----
ord()函数获取字符的整数表示
chr()函数把编码转换为对应的字符
----
print(ord('A')) #65
print(chr(66)) #'B'
print('\u4e2d\u6587') #'中文'

----
'ABC' #str
b'ABC' #bytes  每个字符只占用一个字节
----
以Unicode表示的str可以通过encode()方法编码为9指定的bytes
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ASCII'))
为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#格式化输出字符串
print('hello, %s' % 'world')

#常见的占位符
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
#转义%使用%%
