# x = 3
# print(x)
# print("my name is {0} and age is {1}".format("muhammad", 25))
# name, age = "Muhammad", 30
# print(f'my name is {name} and age is {age} years old')

# anything will be a string in input()
# z = input("please enter your number ")
# # print(z, type(z))
# list1 = [10, 'iti', ['python', 'c++']]
# # print(list1[2][0])
# # del list1[0]
# # print(list1, len(list1))
# list1 += [1, 2, 3]
# print(list1 * 2)
# print(4 in list1)
# print(list1.count("iti"))
# list1.insert(0, 10)
# a = list1.pop()
# print(list1, a)
# list1.reverse()
# list1 = [10,1,9,3,2,5]
# list1.sort()
# print(list1)
# x = 3
# if x > 3:
#     print("3")
# elif x < 3:
#     print("ma4i")
# else:
#     print("ya za3im")
# lis = [0, 2, 3, 7, 9, ['x', 'y']]
# for i in range(len(lis)):
#     print(lis[i])
# i = 0


# while i < len(lis):
#     print(lis[i])
#     i+=1

# flag = True
# while flag:
#     print(lis[i])
#     if i == len(lis):
#         flag = False
#     i+=1
# def welcome():
#     print('hello world')
#
# welcome()
#
# def add(a, x = 5):
#     return a + x
#
# z = add(3)
# print(z)

# def myFun(*arg):
#     print(arg)
#     for val in arg:
#         print(val)
#
# myFun(1,2,3,4,5,5,6,6,6,6)

# try:
#     #print(x)
#     print("try")
# except Exception as e:
#     print(e)
# else:
#     print("else")
# finally:
#     print("finally")
# import mymodule
# from mymodule import *
#
# mymodule.print_fun("abdelhay")
# print(mymodule.person)

# class Employee:
#     Name = "abdelhay"
#
#     def __init__(self, name, age=25):
#         self.Name = name
#         self.age = str(age)
#         print('constructor called ' + self.Name + ' age is ' + self.age)
#
#     def welcome_method(self):
#         print("hello method")
#
#     @staticmethod
#     def print_msg():
#         print("static method")
#
#     @classmethod
#     def class_method(cls):
#         print("class method")
#
#     def __del__(self):
#         print("destructor called")
#
#
# obj = Employee("samir")
# print(obj)
# obj.welcomeMethod()
# obj.job = "developer"
# print(obj.Name + " " + obj.age + " its job is " + obj.job)
# del obj.job
# print(Employee.Name)
# print(hasattr(obj, 'job'))
# print(hasattr(obj, 'Name'))
# attr = getattr(obj, 'age')
# print(attr)
# print(Employee.__dict__)

# class child(parent):

