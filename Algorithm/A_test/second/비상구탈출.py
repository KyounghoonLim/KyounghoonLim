def find_exit(i, j):
    for t1 in range(N):
        for t2 in range(N):
            if test_case[t1][t2] == 2:
                person[-1].append((abs(t1-i)+abs(t2-j), t1, t2))


def my_max(arr):
    maxi = arr[0][0]
    for t1 in range(len(arr)):
        for t2 in range(len(arr)):
            if maxi < arr[t1][t2]:
                maxi = arr[t1][t2]
    return maxi


def min_time(idx=0, times=[]):
    global ans

    if idx == len(person):
        times = sorted(times)
        result = [[0]*N for _ in range(N)]
        for t in range(len(person)):
            if result[times[t][1]][times[t][2]] <= times[t][0]:
                result[times[t][1]][times[t][2]] = times[t][0] + 1
            else:
                result[times[t][1]][times[t][2]] += 1
        max_time = my_max(result)
        if ans > max_time:
            ans = max_time
        return
    for temp in person[idx]:
        times.append(temp)
        min_time(idx+1, times)
        times.pop()


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    person = []

    for i in range(N):
        for j in range(N):
            if test_case[i][j] == 1:
                person.append([])
                find_exit(i, j)

    ans = 999999
    min_time()

    print('#{} {}' .format(tc, ans))