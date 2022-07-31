n = int(input())

money = 1000 - n

lst = [500,100,50,10,5,1]
count = 0
for i in lst:
    count += money//i
    money %= i

print(count)