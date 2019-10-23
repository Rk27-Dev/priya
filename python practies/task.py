# class EvenStream(object):
#     def __init__(self):
#         self.current = 0

#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return

# class OddStream(object):
#     def __init__(self):
#         self.current = 1

#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return

# def print_from_stream(n, stream=EvenStream()):
#     for _i in range(n):
#         if n%2==0:
#             print(stream.get_next())
#         elif n%2!=0:
#               print(stream.get_next())

# queries = int(input())
# for _ in range(queries):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())


# a=int(input('enter value'))
# if a>1:
#     for i in range(2,a):
#         if (a%i)==0:
#             print(' not prime')
#             # print(i,a//i,a)
#             break
#     else:
#             print('prime ')
# else:
#     print('not prime ')



# n=int(input('enter ur value:'))
# for a in range(1,n+1):
#     if a>1:
#         for i in range(2,a):
#             if (a%i)==0:
#                 # print('not prime')
#                 break
#         else:
#              print(a)

# sum of the natural nums 
# n=16
# k=0
# for i in range(n+1):
#     k+=i
# print(k)

# factorial
# s='hello gd morniiing'
# v='aeiou'
# c=0
# for i in s:
#     if i not in v:
#         print(i)
#     else:
#         pass
#         c=c+1
# print(c)


# fact=1
# n=int(input('enter value'))
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)
n=10
for i in range(n+1):
    print((n-i)*" "+ ' #'*i)       
