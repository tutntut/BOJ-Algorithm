n = int(input())
A = list(map(int,input().split()))
B = list(map(int, input().split()))

sum = 0
for i in range(n):
    new_B = max(B)
    new_A = min(A)
    sum += new_B*new_A
    B.remove(new_B)
    A.remove(new_A)

print(sum)