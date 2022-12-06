import math
def f(x):
    return x*math.e**(-x)

a = -100
b = 100
r = (5**0.5 - 1)/2
for i in range(100):
    c = a + r*(b-a)
    d = b + r*(a-b)
    if(f(c) > f(d)):
        a = d
    else:
        b = c
print('x* = ',(a+b)/2)