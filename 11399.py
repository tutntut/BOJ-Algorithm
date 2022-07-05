n = int(input())
lst = list(map(int, input().split()))

lst.sort()

sum, total = 0, 0

for i in range(n):
    sum += lst[i]
    total += sum
    
print(total)