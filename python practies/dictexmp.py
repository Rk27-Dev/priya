# s='hello ravi ho are u'
# d={}
# for x in s:
#     d[x] = d.get(x, 0) + 1
# for k,v in d.items():
#     print(k,"occurred ",v," times")

# sorting of dict
# import operator
# d = {1: 2, 3: 4, 4: 20, 2: 1, 0: 0}
# sorted_d = sorted(d.items(), key=operator.itemgetter(0))
# print('ascending order : ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(0),reverse=True))
# print(' descending order  : ',sorted_d)
#
# dict concatination
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# dic4 = {}
# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic1)

# Write a Python program to check if a given key already exists in a dictionary?
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # print(6 in d)
# def f1(a):
#     if a in d:
#         print('Key is present in the dictionary')
#     else:
#         print(' Key not present in the dictionary')
# f1(10)
# f1(2)

# iteration of dict
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for i in d:
#     print(d)
#

# n=15
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)
#

# d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# # print(sum(d.keys()))
# # print(sum(d.values()))
# mul=1
# add=0
# for key,value in d.items():
#     mul=mul*d[key]
#     add=add+d[key]
# print(mul,add)

# mapping two lists into dict
# l=[1,2,3,4,5,6,7,8,9]
# m=[10,20,30,40,50,60,70,80,90]
# print(dict(zip(l,m)))
#  sorting based on key

# Write a Python program to get the maximum and minimum value in a dictionary
# d = {1: 2, 3: 4, 4: 20, 2: 1, 0: 0}
# print(max(d.keys()))
# print(max(d.values()))

# Write a Python program to remove duplicates from Dictionary.
# d = {1: 2, 3: 4, 4: 20, 2: 1, 0: 0,1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# l={}
# for k,v in d.items():
#     if d not in l.values():
#         l[k] = v
#         print(l)

# Write a Python program to check a dictionary is empty or not
# d={}
# if not bool(d):
#     print("Dictionary is empty")
#
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for k,v in d2.items():
#     if d1 not in d2.values():
#         d1[k]=v
# print(d1)

# data =[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print(set(data))

import itertools

# d = {'1': ['a', 'b'], '2': ['c', 'd']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))

# Write a Python program to find the highest 3 values in a dictionary.

# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result=nlargest(3,my_dict,key=my_dict.get)
# print(result)

# d={}
# c=0
# s='hello how are u'
# for i in s:
#     if ' ' :
#          c=c+1
# print(c)


# s='hello ravi how are u please ravi tell me how about u'
# d={}
# c=0
# for i in s.split():
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#     c+=1
# print(d)
# print(c)

# palindrom

# s='1232451'
# k=s[::-1]
# if s==k:
#     print('palindrome')
# else:
#     print('not pali')

# factorial of n
# n=int(input('enter ur num:'))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)
#
# import math
# print(math.factorial(6))


# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
# n1 = 0
# n2 = 1
# count = 0
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence upto",nterms,":")
#    while count < nterms:
#        print(n1,end=' , ')
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


# prime nums range bw
# for num in range(1,100):
   # prime numbers are greater than 1
# for num in range(1,20):
# # num=int(input('enter your num:'))
#
#     if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                # print('not prime')
#                break
#        else:
#            print(num,'prime')

# armstong
# n=153
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     print(digit)
#     sum+=digit**3
#     temp//=10
# if sum==n:
#     print('armsrong')
# else:
#     print('not armsrong')
# print(4**3)

# s='google.com'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)