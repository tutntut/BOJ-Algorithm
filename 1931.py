n = int(input())

lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a,b])

lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x : x[1])


check = lst[0][1]
count = 1
for i in range(1,n):
    if lst[i][0] >= check:
        count += 1
        check = lst[i][1]

print(count)
