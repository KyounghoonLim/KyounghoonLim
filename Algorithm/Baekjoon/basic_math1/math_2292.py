N = int(input().strip())

r = 0
temp = 1
while N > temp:
    r += 1
    temp += 6 * r

print(r+1)