def conv(string):
    result = []
    for i in range(len(string)):
        result.append(int(string[i]))
    return result


gears = [conv(input().strip()) for _ in range(4)]
K = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(K)]

for do in test_case:
    rotate = [False] * 4
    Q = [[do[0]-1, do[1]]]
    while Q:
        gear = Q.pop(0)
        rotate[gear[0]] = gear[1]
        if gear[0] > 0 and not rotate[gear[0]-1] and gears[gear[0]][6] != gears[gear[0]-1][2]:
            Q.append([gear[0]-1, gear[1] * -1])
        if gear[0] < 3 and not rotate[gear[0]+1] and gears[gear[0]][2] != gears[gear[0]+1][6]:
            Q.append([gear[0]+1, gear[1] * -1])
    for t in range(4):
        if rotate[t] < 0:
            gears[t] = gears[t][1:] + [gears[t][0]]
        elif rotate[t] > 0:
            gears[t] = [gears[t][-1]] + gears[t][:-1]

ans = 0
for n in range(4):
    ans += gears[n][0] * 2 ** n

print(ans)