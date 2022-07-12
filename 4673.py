def self_number(n):
    number = n
    for i in list(str(number)):
        number += int(i)
    return number

arr = []

for i in range(10000):
    arr.append(self_number(i))
    
for j in range(10000):
    if j in arr:
        continue
    else:
        print(j)
    