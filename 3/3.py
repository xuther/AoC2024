import re

expression = "(mul\((\d+),(\d+)\))|(don\'t\(\))|(do\(\))"

val = re.compile(expression)

total = 0

with open("3/3.in") as f:
    on = True
    for line in f.readlines():
        matches = val.findall(line)
        for match in matches:
            if match[3] == "don't()":
                on = False
            elif match[4] == "do()":
                on = True
            elif on == True:
                total += (int(match[1]) * int(match[2]))
            
            
print(total)
            