def is_in(n):
    for t in visited:
        if n == t:
            return
    return True


test_case = [int(input().strip()) for _ in range(10)]
temp = []
visited = []
cnt = 0
for num in test_case:
    temp.append(num % 42)
for i in range(1, 10):
    if temp[0] != temp[i] and is_in(temp[i]):
        cnt += 1
        visited.append(temp[i])

print(cnt+1)