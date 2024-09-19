# from socketserver import DatagramRequestHandler
# from struct import pack_into
#
# from PyQt5.QtGui.QRawFont import descent

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


# class A:                    #method overloading
#
#     def test(self, a):
#         print(a)
#
#     def test(self,a,b):
#         print(a+b)
#
#     def test(self,a,b,c):
#         print(a+b+c)
#
#
# a = A()
# a.test(2)
# a.test(1,2)
# a.test(1,2,3)


# class Emp:
#     _pin=1234
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



