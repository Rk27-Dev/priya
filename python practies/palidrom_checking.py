num=input('Enter num:-')
num1=num
count1=0
while True:
    if num==num[::-1]:
        high=num
        break
    else:
        count1+=1
        num=int(num)
        num+=1
        num=str(num)
count2=0
while True:
    if num1==num1[::-1]:
        low=num1
        break
    else:
        count2+=1
        num1=int(num1)
        num1-=1
        num1=str(num1)
                
if count1>count2:
    print(low)
else:
    print(high)
