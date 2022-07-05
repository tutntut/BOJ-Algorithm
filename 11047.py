n, k = map(int, input().split())
lst = []
for i in range(n):
    b = int(input())
    lst.append(b)

lst.sort(reverse = True)

num = 0

for coin in lst:
    num += k // coin
    k = k%coin

print(num)