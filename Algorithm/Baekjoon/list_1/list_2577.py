test_case = [int(input().strip()) for _ in range(3)]
cnt = [0] * 10
temp = str(test_case[0] * test_case[1] * test_case[2])

for i in temp:
    cnt[int(i)] += 1

for t in cnt:
    print(t)