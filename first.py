from numpy import *
from numpy.f2py.crackfortran import endifs
from numpy.ma.extras import row_stack
from pandas.core.dtypes.base import StorageExtensionDtype
from selenium.webdriver.common.devtools.v85.log import stop_violations_report
from setuptools.command.build_ext import if_dl

print('hello world')

# for i in range(1, 15):
#     if i == 10:
#         break
#     else:
#         print(i)

# a = 1
#
# while a <= 15:
#     print(a)
#     a = a+1
#
# print('done')

# for i in range(0, 21, 2):
#     print(i)

# num = int(input('enter : '))
# rev = int(str(num)[::-1])
# if num == rev:
#     print('palindrom')
# else:
#     print('not')

# a =[]
# b ={'a':'1', 'b':'2'}
# c = {'c':'3'}
# a.append(b)
# a.append(c)
# print(a)

# class A:
#
#     def fun1(self):
#         print('feature_1 of class A')
#
#     def fun2(self):
#         print('feature_2 of class A')
#
#
# class B(A):
#
#     # Modified function that is
#     # already exist in class A
#     def fun1(self):
#         print('Modified feature_1 of class A by class B')
#
#     def fun3(self):
#         print('feature_3 of class B')
#
#
# # Create instance
# obj = B()
#
# # Call the override function
# obj.fun1()


# class A:           #method overriding
#
#     def test1(self):
#         print('class A method')
#
# class B(A):
#     def test1(self):
#         super().test1()
#         print('class B method')
#
# b= B()
# b.test1()


# class A:                    #method overloading not possible in python in this it will access only latest method
#
#     def test(self, a):
#         print(a)
#
#     def test(self,a,b):
#         print(a+b)
#
#     def test(self,a,b,c=0):
#         print(a+b+c)
#
#
# a = A()
# a.test(2)
# a.test(1,2)
# a.test(1,2,3)   # only this will work


# class Emp:
#     _pin=1234      #protected variable
#     def _disp(self):
#         print('this is protected')
#
#     def getter(self):
#         return self._pin
#
#     def setter(self, pin):
#         self._pin= pin
#
#
# e = Emp()
# pin = e.getter()
# print(pin)
# e.setter(5678)
# pin=e.getter()
# print(pin)

#row = int(input('enter : '))

# for i in range(1, row+1):
#         print('*' * i)
#
# for i in range(row, 0, -1):
#         print('*' * i)


# for i in range(1, row+1):
#         # Print spaces for alignment
#         print(' ' * (row - i), end='')
#         # Print stars
#         print('*' * (2 * i - 1))
#
# for i in range(row, 0, -1):
#         # Print spaces to center the stars
#         print(' ' * (row - i), end='')
#         # Print stars
#         print('*' * (2 * i - 1))



#PALINDROM#
# num = int(input("enter : "))
# rev_num = int(str(num)[::-1])
# if num == rev_num:
#     print("palindrom")
# else:
#     print('not palindrom')

# a =[int(i) for i in input("enter seperated by spaces").split()]
# b= []
# for i in a:
#     c= sum(int(digit) for digit in str(i))
#     b.append(c)
# print(b)
# import numpy as np
# import pandas as pd
#
# from green_cart import count

# abc = [1, 2, 3, 4, 5, 6]
# a = np.array(abc)
# print(a.shape)
# print(a)
# arr1 = np.linspace(1,3,10)
# print(arr1)

# s = pd.Series(range(1,16,3), index=[x for x in 'abcde'])
# print(s)
# a = int(input('enter : '))
# if a>1:
#     for i in range(2, a):
#         if (a % i) == 0:
#             print('not prime')
#         else:
#             print('prime')
# else:
#     print('not prime')

# from functools import reduce
# nums = [1,2,3,4,5,6,7,8,9]
#
# evens = list(filter(lambda n : n%2==0, nums))
# print(evens)
#
# squre = list(map(lambda n : n**2, nums))
# print(squre)
#
# addition = reduce(lambda a,b: a+b, nums)
# print(addition)


# def addition(a,b):
#     return a+b
# def multification(addition):
#     print(addition * 2)
#
#
# multification(addition(2,3))

# a = 'aabbbccc'
# dicte = {}
# for i in a:
#     count= a.count(i)
#     dicte[i] = count
# print(dicte)

# class Numbers():
#     number = 1234
#
#     def first(self):
#         print(self.number)
#
#     @classmethod
#     def second(cls):
#         cls.number = 5678
#         print(cls.number)
#
# num = Numbers()
# num.second()
# num.first()

# i = 1
# count=0
#
# while count <= 30:
#     i=i*2
#     count+=1
# print(i)


# numbers = [[34, 63, 88, 71, 29], [90, 78, 51, 27, 45], [63, 37, 85, 46, 22], [51, 22, 34, 11, 18]]
#
# averages = list(map(lambda num_list: sum(num_list)/len(num_list), numbers))
# print(averages)


# def prime_number(num):
#     if num < 1:
#         return False
#     for i in range(2,int(num//2)+1):
#         if num % i == 0:
#             return  False
#     return True
#
# # num = int(input('enter number : '))
# # print(f"{num} is prime (true or false) : {prime_number(num)}")
# a =[]
# for i in range(101):
#     if prime_number(i):
#         a.append(i)
#
# print(a)

# print('hello ',end='')
# print('india')

# class Abc():
#     def __init__(self, name):
#         self.name = name
#
#
# a =Abc('akash')
# print(a.name)

# name = ['akash']
# for i in name:
#     if i[0] == 'a':
#         print('True')
#     else:
#         print('false')

# Dictionary comprahension
# users = [(0,'abc','sdf'),(1, 'dfdf','dafh'),(2, 'dhj','uyt')]
#
# new_user = {user[1]: user for user in users}
# print(new_user)


# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# def subtract(*args):
#     result = args[0]
#     for num in args[1:]:
#         result -= num
#     return result
#
# def calculation(*args, operator):
#     if operator == '*':
#         print(multiply(*args))
#     elif operator == '+':
#         print(sum(args))  # sum is a built-in function
#     elif operator == '-':
#         print(subtract(*args))
#     else:
#         print('Give valid input')
#
# # Corrected function call
# calculation(*(1, 2, 3, 4), operator='+')


# def outer_function(**kwargs):
#     inner_function(**kwargs)

# def inner_function(**kwargs):
#     print(f" {kwargs['name']},  {kwargs['age']}")
#
# inner_function(name="Bob", age=25)



# a = (1,2,3,4,5)
# def calculatio(*args):
#     print(sum(*args))
#
# calculatio(a)


from typing import *
# def list_avg(num):
#     return (sum(num) / len(num))
#
# print(list_avg([1,2,3]))



# a = [int(i) for i in input("enter: ") if int(i) % 2 == 0]
# print(a)

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([1,10])
# y = np.array([2, 10])
#
# plt.scatter(x, y)
# plt.show()
#

#
# row = int(input('enter: '))
#
# start = 1
# for i in range(1, row):
#     for j in range(i):
#         print(start, end=" ")
#         start += 2
#     print()

# print(0.1 + 0.2 == 0.3)



def is_leap_year(year):
    # A leap year is divisible by 4, except for end-of-century years, which must be divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


