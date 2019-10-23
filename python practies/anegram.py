f = open('sample.txt', 'r')
t = f.read().split()
d = {}
for i in t:
    x = sorted(i)
    for j in t:
        if i != j:
            y = sorted(j)
            if x == y:
                if i not in d:
                    d[i] = [j]
                else:
                    d[i].append(j)


# dog

# god