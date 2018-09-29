#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['yaodaxia','yaoyawei','huangying']
for name in names:
    print(name)

# example:for
print("#----example:for----")
sum =0
for i in range(101):
    sum = sum + i
print(sum)

# example:while
print("----example:while----")
sum1 = 0
n = 100
while n>0:
    sum1 = sum1 + n
    n = n - 1
print(sum1)

# example:break
print("----example:(while)break----")
sum2 = 0
i2 = 0
while i2<101:
    i2 = i2 + 1
    if i2==10:
        break
    sum2 = sum2 + i2
print(sum2)
print("----example:(for)break----")
sum3 = 0
for i3 in range(101):
    if i3==10:
        break
    sum3 = sum3 + i3
print(sum3)

# example:continue
print("----example:(while)continue----")
sum4 = 0
i4 = 0
while i4<100:
    i4 = i4 + 1
    if i4==10:
        continue
    sum4 = sum4 + i4
print(sum4)
print("----example:(for)continue----")
sum5 = 0
for i5 in range(101):
    if i5==10:
        continue
    sum5 = sum5 + i5
print(sum5)

# example:dic & set
print()
dictionary = {'yaodaxia':617,'yaoyawei':431,'huangying':543}
print(dictionary['yaodaxia'])
