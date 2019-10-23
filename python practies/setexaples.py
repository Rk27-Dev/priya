# s={10,1,2,3,4,5,6}
# t={20,90,630,45,9,6,3}
# print(s.union(t))
#
# print("diff",s.difference(t))
# print("intersection",s.intersection(t))
# print("symetric",s.symmetric_difference(t))

#membership operators
# # in /not in
# a={10,50,60,80}
# b=20
# print( b in a)
# idetity operators
# a=20
# b=20
# print(a is b)
s={1,2,6,5,9,7,80,90,12}
k={k*k for k in s }
print(k)