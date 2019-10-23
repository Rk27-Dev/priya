# def f1(a):
#     print('fun',a)
# f1(a=10)
#
#
# even num odd
# def f1(n):
#     if n%2==0:
#         print('even num')
#     else:
#         print('odd num!!')
# n=int(input('enter ur value!!'))
# f1(n)

# def f1(*n):
#     for i in n:
#         print(i)
# f1(1,2,3,4,5,6)
#
# def f1(**n):
#     # for i in n:
#     #     print(i)
#     print(n)
# f1(a=1,b=2,c=3,d=4,e=5,f=6)

# global nd local variables
# a=20
# def f1():
#     a=50
#     print(a)
# f1()
# print(a)

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

#
# k=lambda x,y:x+y
# print(k(5,10))


# l=lambda a,b:a if a>b else b
# print(l(90,50))

# l=[2,3,6,4,5,8,9,78,45,6,62,45,8,96,12]
# l=list(filter(lambda x: x%3==0, l))
# print(l)
#
# l=[2,6,46,89,71,46,79,7,89]
# k=list(map(lambda x:x*x,l))
# print(k)
#
# from functools import *
# l=[2,6,46,89,71,46,79,7,89,78,45,6,62,45,8,96,12]
# l=reduce(lambda x,y:x+y,l)
# print(l)

# nested functions
# global a
# a=50
# def f1():
#     global a
#     a=20
#
#     print('f1',a)
#     def f2():
#         global a
#         a = 15
#         b=65
#         print('f2',a,b)
#     return f2()
# f1()


#
# class toosmall(Exception):
#     # print('to small')
#     pass
# class Toolarge(Exception):
#     # print('to large exception')
#     pass
# try:
#     a=10
#     b=20
#     if a>=b:
#         raise toosmall
#     else:
#         raise Toolarge
#
# except :
#     raise Toolarge


# sum of natural nums
# n=10
# sum=0
# for i in range(n+1):
#     sum=sum+i
#     print(sum)

#fibanaci seriece
n=10
n1=0
n2=0
count=0
if n<0:
    print('enter positive values')
elif n==1:
    print('fibanaci values upto', n)
    print(n1)
else:
    print('fibanaci values upto',n)
    print(n1)
    while count<n:
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


