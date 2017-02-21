import math
import os
import string
print(abs(-20))

print(max(1, 2))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('必须是数字')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(my_abs(-10))
#print(my_abs('haha'))
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#神一样的逻辑
def add_end(L=[]):
    L.append('END')
    return L
L1=[1, 2, 3]
add_end(L1)
print(L1)
#接下来神奇的一幕！
print(add_end())
print(add_end())
print(add_end())
print(add_end())

#原因解释如下：

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

#要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())

#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
print(calc(1, 2, 3))
#或者
nums = [1, 2, 3]
print(calc(*nums))

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(extra['job'])
person('Bob', 35, city='Beijing',job=extra['job'])


#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact_iter(5, 1))
d={'a':1,'b':2,'c':'3'}
for key in d:
    print(key)

for key in d.values():
    print(key)
for k, v in d.items():
    print(k, v)
for x,y in [(1,2),(2,3),(3,4)]:
    print(x,y)
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('.')])
#转小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
L1=['我','特','么','饿','了']
L2=[s+' !' for s in L1]
str_convert = ''.join(L2)
print(str_convert)
str='但是 我饿了啊 fuck'
list = list(str)
L2=[s+' !' for s in list]
str_convert = ''.join(L2)
print(str_convert)