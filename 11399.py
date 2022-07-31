n = int(input())
lst = list(map(int, input().split()))

lst.sort(key = lambda x : x)
sum = 0
answer = 0
for i in lst:
    sum += i
    answer += sum

print(answer)