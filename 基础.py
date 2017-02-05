from 函数 import my_abs
print("hello world")
100+200
print('The quick brown fox', 'jumps over', 'the lazy dog')
name = input()
print(name)
name = input('please enter your name: ')
print('hello,', name)
print('1024 * 768 = ', 1024*768)

a = -100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m ok.')

print('I\'m learning\nPython.')
#普通除
10 / 3
#地板除
10 // 3
#字符集
ord('A')
ord('中')
chr(66)
chr(25991)
'\u4e2d\u6587'

'中文'.encode('utf-8')

b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')


#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
'Hello, %s' % 'world'

'Hi, %s, you have $%d.' % ('Michael', 1000000)

'%2d-%02d' % (3, 1)

'%.2f' % 3.1415926

'Age: %s. Gender: %s' % (25, True)

'growth rate: %d %%' % 7

classmates = ['Michael', 'Bob', 'Tracy']
classmates


s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#range(101)就可以生成0-100的整数序列，计算如下：
sum = 0
for x in range(101):
    sum = sum + x
    print(sum)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']