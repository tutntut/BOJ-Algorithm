num, money = map(int, input().split())
lst = []
for i in range(num):
    a = int(input())
    lst.append(a)

lst.sort(key = lambda x : -x)
count = 0

for i in lst:
    count += money // i
    money %= i

print(count)

