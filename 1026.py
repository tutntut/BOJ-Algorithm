n = int(input())
A = list(list(map(int, input().split())))
B = list(list(map(int, input().split())))

A.sort()

sum = 0

for i in range(n):
    maximum = max(B)
    sum += int(A[i]) * int(maximum)
    B.remove(maximum)


print(sum)

#값을 지우려면 pop이 아닌 remove!!