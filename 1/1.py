from collections import defaultdict

v1 = []
v2 = defaultdict(int)

with open("1/1.in") as f: 
    for line in f.readlines():
        tmp = line.split()
        v1.append(int(tmp[0]))
        v2[int(tmp[1])] = v2[int(tmp[1])]+1


total = 0
for i in range(len(v1)):
    t = v1[i]
    x = v2[t]
    total = total + (t * x)
    
print(total)
    
    