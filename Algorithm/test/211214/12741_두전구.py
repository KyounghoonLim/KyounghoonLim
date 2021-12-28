ans = []
for tc in range(1, int(input())+1):
    A, B, C, D = map(int, input().split())
    ans.append(max(0, min([B, D]) - max([A, C])))

for i in range(len(ans)):
    print('#{} {}' .format(i+1, ans[i]))