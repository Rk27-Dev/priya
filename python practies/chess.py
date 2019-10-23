n = raw_input("enter q for queen and h for horse")
l = [1, 2, 3, 4, 5, 6, 7, 8]
if n == 'q':
    x1 = int(input('enter starting position first element'))
    y1 = int(input('enter starting position second element'))
    x2 = int(input('enter ending position first element'))
    y2 = int(input('enter ending position second element'))
    if (x1 in l) and (y1 in l):
        if (x2 in l) and (y2 in l):
            x = x2 - x1
            y = y2 - y1
            if (x == 0 or y == 0) or ((x + y) == 2 * x or (x - y) == 0 or (x + y) == 0):
                print "valid move"
            else:
                print "invalid move"
    else:
        print "position is in out of board"
elif n == 'h':
    x1 = int(input('enter starting position first element'))
    y1 = int(input('enter starting position second element'))
    x2 = int(input('enter ending position first element'))
    y2 = int(input('enter ending position second element'))
    if (x1 in l) and (y1 in l):
        if (x2 in l) and (y2 in l):
            x = x2 - x1
            y = y2 - y1
            nm = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
            if (x, y) in nm:
                print "valid move"
            else:
                print "invalid move"
    else:
        print "position is in out of board"
else:
    print "choose only q or h"
