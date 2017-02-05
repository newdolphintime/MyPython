import math
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