l = ['srh', 'mi', 'chn', 'kkr', 'dd', 'rr', 'rcb', 'kxip']
c = 0
for i in l:
    for j in l:
        if i != j:
            c = c + 1
            print (i, j)
print c
