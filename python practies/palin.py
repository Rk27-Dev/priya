# how many types we can solve palindrome


# first method
p = raw_input("enter a word for find whether it is pal or not")
if p == p[0:0:-1]:
    print "palindrome"
else:
    print "not palindrome"

# second method
if p == reversed(p):
    print "palindrome"
else:
    print "not palindrome"

# third method
l = list(p)
print l
h=l.reverse
print h
if l == h:
    print "palindrome"
else:
    print "not palindrome"

# fourth method
s = ""
#madam
for i in p:
    s = i + s
if p == s:
    print "palindrome"
else:
    print "not palindrome"
