# from twilio.rest import Client
# import math, random 
# def f1():
#     account_sid = 'AC3a846e5983cc3d62b4c303813b605241'
#     auth_token = 'd66ca53f3f3ada42adf222a420a70fda'
#     client = Client(account_sid, auth_token)
#     digits = "0123456789"
#     OTP = "" 
#     for i in range(4) : 
#         OTP += digits[math.floor(random.random() * 10)] 
#     message = client.messages \
#         .create(
#              body='dont share with any one'+" "+OTP,
#              from_='+12056276621',
#              to='+91-9533558978'
#          )
# f1()

# sum=0
# num=153456
# temp=num
# while  temp>0:
#   didgit=temp%10
#   print(didgit)
#   sum+=didgit**3
#   temp=temp//10
# if num==sum:
#     print('armstong')
# else:
#      print('not armstong')


# def fact(n):
#     if n==1:
#         return n
#     else:
#         n*fact(n-1)
# f=fact(5)
# print(f)

x = ["abbbb","123a","nnnnas"]
for i in x:
	s=i[0]
	e=i[-1]
	u='_'*(len(i)-2)
	n=s+u+e
	print(n)
	
