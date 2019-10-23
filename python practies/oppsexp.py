# class c:
#     a=10
#     b=20
#     def m1(self):
#         print(c.a)
#         print(c.b)
# a1=c()
# a1.m1()

# class hai():
#     a=20
#     b=60
#     def __init__(self):
#         self.a=100
#         self.b=1
#     def m2(self):
#         print(hai.a)
#         print(hai.b)
#     def m1(self):
#         print (self.a)
#         print (self.b,"hello")
# h=hai()
# h.m1()
# h.m2()
# g=hai()
# g.m1()
# g.m2()
# class x():
#     a=50
#     def __init__(self):
#         print('cont')
#
#     def m1(self):
#         print('method')
#         print(x.a)
#
# class y(x):
#     def __init__(self):
#         print('hello')
#     def m2(self):
#         self.a=40
#         print('method....2' ,self.a)
# y1=y()
# y1.m2()
# y1.m1()
# overloading
# class c1():
#     a=60
#     def m1(self):
#         print('m1')
#     def m1(self,a):
#         self.a=60
#         print(self.a)
#     def m2(self,a,b):
#         self.a=20
#         self.b=90
#         print(self.a)
#         print(self.b)
#
# c=c1()
# c.m2(a=30,b=60)

# over riding


# class x:
#     def m1(self):
#         print('method 1')
#     def m2(self):
#         print('method2')
# class y1(x):
#     def m3(self):
#         # self.m1()
#         super().m1()
#         print('method3')
# y=y1
# y.m3()
#

#
# multi threading concept
import threading
class c(threading.Thread):
    def run(self):
        for i in range(1,5):
            print(i)
class d(threading.Thread):
    def run(self):
        for j in range(50,55):
            print(j)
d1=d()
c1=c()
d1.start()
c1.start()


