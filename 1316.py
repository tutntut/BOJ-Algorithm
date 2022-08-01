n = int(input())
count = 0

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            lst = word[j+1:]
            if word[j] in lst:
                count += 1
                break

result = n - count

print(result)

