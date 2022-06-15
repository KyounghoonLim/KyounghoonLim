import math

N = int(input())
people = list(map(int, input().split()))
watchers = list(map(int, input().split()))

ans = 0

for i in range(N):
    if people[i] > watchers[0]:
        ans += math.ceil((people[i] - watchers[0]) / watchers[1]) + 1
    else:
        ans += 1

print(ans)