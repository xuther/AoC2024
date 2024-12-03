safeCount = 0


def CheckSafe(i, depth):
    n = i[0]
    d = 0
    for j in range(1,len(i)):
        cur = n
        n = int(i[j])
        diff = n - cur 
        if d == 0:
            if diff == 0:
                if depth == 0:
                    new = i.copy()
                    new.pop(j)
                   # Check if we're safe if we remove either this or the previous value.
                    if CheckSafe(new,1):
                       return True
                    new = i.copy()
                    new.pop(j-1)
                    if CheckSafe(new,1):
                       return True
                return False
            if diff < 0:
                d = -1
            else:
                d = 1
        if d == -1:
            if 0 > diff  and diff > -4:
                continue
            else:
                if depth == 0:
                    new = i.copy()
                    new.pop(j)
                   # Check if we're safe if we remove either this or the next value.
                    if CheckSafe(new,1):
                       return True
                    new = i.copy()
                    new.pop(j-1)
                    if CheckSafe(new,1):
                       return True
                return False
        elif d == 1:
            if 0 < diff  and diff < 4:
                continue
            else:
                if depth == 0:
                    new = i.copy()
                    new.pop(j)
                   # Check if we're safe if we remove either this or the next value.
                    if CheckSafe(new,1):
                       return True
                    new = i.copy()
                    new.pop(j-1)
                    if CheckSafe(new,1):
                       return True
                return False
    return True


with open("2/2.in") as r:
    l = 0
    for i in r.readlines():
        k = i.split()
        safe0 = CheckSafe([int(j) for j in k], 0)
        if safe0:
            safeCount = safeCount+1 
        #print(l, " is ", safe0)
        l += 1

print(safeCount)