n = int(input())

count = 0

while True:
    if n % 5 == 0:
        count += n // 5
        break
    elif n == 0:
        break
    elif n < 0:
        count = -1
        break
    else:
        count += 1
        n -= 3

print(count)


'''
while n >= 0:
    if n %5 ==0:
        count += (n //5)
        print(count)
        break
    n -= 3
    count += 1

else:
    print(-1)

'''