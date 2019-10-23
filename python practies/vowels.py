str1 = "my name is pavan kumar"
str2 = " aeiou "
dis  ={}
for x in str1:
         if not x.isspace():
            if x in str2:
               dis.setdefault(x,0)
               dis[x] += 1
print(dis)
