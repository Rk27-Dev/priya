stats = []
d = {}
for i in stats:
    date = i[0].split('/')
    key = (date[1], i[1])
    if key not in d:
        tot_runs = i[4]
        avg_runs = i[4]
        c = 1
        d[key] = [tot_runs, c, avg_runs]
    else:
        d[key][0] = d[key][0] + i[4]
        d[key][1] = d[key][1] + 1
        d[key][2] = d[key][0] / float(d[key][1])

for i in d.items():
    # i=(month,country),[t]
    print "in the month", i[0][0], "and country", i[0][1], "total runs", i[1][0], "avg runs", i[1][2]
