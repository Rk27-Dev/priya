name=input("enter employee name:")
salary=int(input("enter employee salary:"))
d={}
d["name"]=name
d["salary"]=salary
while(True):
    exp1=input("enter what expense:")
    if exp1=="q":
        break
    amount=int(input("enter amount:"))
    if amount<salary:
        d[exp1]=amount
        tot=salary-amount
        d["rembal"]=tot
        print(tot)
    else:
        print("insufficient balance")
               
print(d)   
