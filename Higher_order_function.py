#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("----函数名----")
f = abs
print("f=abs,f(-10)=%d)"%f(-10))
#abs = 10 #abs(-10)会报错
#print("abs=10,abs(-10)=%d"%abs(-10)) 

f = abs
def add(x, y, f):
    return f(x) + f(y)
#add(5,-6,abs)=abs(5)+abs(-6)=11
print("add(5,-6,abs)=%d"%add(5,-6,abs))

# map() & reduce()
print("----map() & reduce()----")
l_map = [1,2,3,4,5,6,7,8,9]
def cube(x):
    return x*x*x
print("l_map=%s"%l_map)
print("map(cube,l_map)=%s"%map(cube,l_map))
print("map(str,l_map)=%s"%map(str,l_map))
print("map(str,map(cube,l_map)=%s"%map(str,map(cube,l_map)))

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
print("reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)")
def sum_reduce(x,y):
    return x+y
l_reduce = [n for n in range(101)]
print("l_reduce = %s"%l_reduce)
print("reduce(sum_reduce,l_map)=%d"%reduce(sum_reduce,l_reduce))
print("sum(l_reduce)=%d"%sum(l_reduce))

# example:filter()
print("----filter()----")
def is_prime_num(x):
    n = 2
    while(n < x):
        if x%n == 0:
            return False
        else:
            n = n+1
    #print("%d is a prime nummber."%x)
    return True
# test code of is_prime_num        
num_test = 5000    # int(input()) 
#print("%d is a prime nummber:%s"%(num_test,is_prime_num(num_test)))
num_test = [n for n in range(num_test)]
num_test = filter(is_prime_num,num_test)
print("type of num_test is %s"%type(num_test)) # type of filter is <class 'filter'>
print("num_test = filter(num_test):%s"%list(num_test))

# example: sorted()
print("----sorted()----")
print(sorted(['bob', 'about', 'Zoo', 'Credit']))    # 默认按照ASCII的大小比较
print(sorted([36, 5, -12, 9, -21], key=abs))    #
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


