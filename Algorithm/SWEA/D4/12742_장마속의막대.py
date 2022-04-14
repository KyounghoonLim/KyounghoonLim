T = int(input().strip())
ans = []

for tc in range(1, T+1):
    a, b = map(int, input().strip().split())
    _sub = b - a
    num = _sub * (_sub + 1) // 2
    ans.append(num - b)

for i in range(len(ans)):
    print('#{} {}' .format(i+1, ans[i]))