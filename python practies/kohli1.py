stats = []
d = {}
for i in stats:
    if i[2] == "Not Out":
        date = i[0].split('/')
        if date[1] not in d:
            d[date[1]] = 1
        else:
            d[date[1]] = d[date[1]] + 1
for i in d.items():
    print "month is", i[0], "and how many times he was is", i[1]
