#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def __init__(self):
        self.leg = 4
        self.mouth = 1
    def __len__(self):
        return 101
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def __init__(self):
        self.ear = 2
        self.eye = 2
    def __len__(self):
        return 105
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print("isinstance(dog,Dog) = %s"%isinstance(dog,Dog))
print("isinstance(dog,Cat) = %s"%isinstance(dog,Cat))

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

# 多态
print("-----理解多态-----")
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

print("type(Dog) = %s"%type(Dog))
print("type(123) = %s"%type(123))

print("isinstance(dog,Object) = %s"%isinstance(dog,object))
print("isinstance(dog,Animal) = %s"%isinstance(dog,Animal))
print("isinstance(dog,Dog) = %s"%isinstance(dog,Dog))

print("isinstance([1, 2, 3], (list, tuple)) = %s"%isinstance([1, 2, 3], (list, tuple)))
print("isinstance((1, 2, 3), (list, tuple)) = %s"%isinstance((1, 2, 3), (list, tuple)))

print("len(dog) = %d"%len(dog))
print("len(cat) = %d"%len(cat))

# 测试对象的属性和方法
print("dir(Dog) = %s"%dir(Dog))
print("dir(Cat) = %s"%dir(Cat))

# 使用getattr()、setattr()以及hasattr() 操作对象的状态
my_dog = Dog()
my_cat = Cat()
print('----属性操作前----')
# hasattr
print("hasattr(my_cat,'mouth') = %s"%hasattr(my_cat,'mouth'))
print("hasattr(my_cat,'leg') = %s"%hasattr(my_cat,'leg'))
print("hasattr(my_dog,'eye') = %s"%hasattr(my_dog,'eye'))
print("hasattr(my_dog,'ear') = %s"%hasattr(my_dog,'ear'))
# setattr
setattr(my_cat,'leg',4)
setattr(my_cat,'mouth',1)
setattr(my_dog,'eye',2)
setattr(my_dog,'ear',2)
print("----属性操作后----")
print("hasattr(my_cat,'run') = %s"%hasattr(my_cat,'run'))
print("hasattr(my_cat,'leg') = %s"%hasattr(my_cat,'leg'))
print("hasattr(my_dog,'eye') = %s"%hasattr(my_dog,'eye'))
print("hasattr(my_dog,'ear') = %s"%hasattr(my_dog,'ear'))
# getattr
print("getattr(my_dog,'eye') = %s"%getattr(my_dog,'eye'))
print("getattr(my_cat,'leg') = %s"%getattr(my_cat,'leg'))
print("getattr(my_cat,'tail','Oh,my god!') = %s"%getattr(my_cat,'tail','Oh,my god!'))

# 实例属性和类属性的区别
class person(object):
    def __init__(self, name):
        self.name = name

s = person('Bob')
s.score = 90
print("s.score = %d"%s.score)

class Student(object):
     name = 'Student'

s = Student() # 创建实例s
print("----创建实例s----")
print("s.name = %s"%s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print("Student.name = %s"%Student.name) # 打印类的name属性

print("----为实例s绑定name属性----")
s.name = 'Michael' # 给实例绑定name属性
print("s.name = %s"%s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问

print("----删除实例s的name属性----")
del s.name # 如果删除实例的name属性
print("s.name = %s"%s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print("----实例属性和类属性的总结：----")
print("在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。")
