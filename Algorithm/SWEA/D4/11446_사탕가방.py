def change(idx):
    res = test_case[idx] // ratio[idx]
    test_case[idx] %= ratio[idx]
    return res


T = int(input().strip())

for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    test_case = list(map(int, input().strip().split()))

    if sum(test_case) < M:
        print('#{} 0' .format(tc))
        continue

    ans = 0
    flag = 0
    while not flag and sum(test_case) > M:
        for t in range(N):
            if not test_case[t]:
                flag = 1
                break
        if not flag:
            test_case.sort()
            ratio = test_case.copy()
            mini = test_case[0]
            for idx in range(N):
                ratio[idx] /= mini
            sigma = sum(ratio)
            if sigma > M:
                ans = mini
                break
            elif sigma < M:
                ratio_r = []
                temp = M / sigma
                for idx in range(N):
                    ratio[idx] *= temp
                    ratio_r.append(int(ratio[idx]))
                while sum(ratio_r) < M:
                    maxi = 0
                    for idx in range(N):
                        if ratio[idx] - int(ratio[idx]) > ratio[maxi] - int(ratio[maxi]):
                            maxi = idx
                    ratio[maxi] = int(ratio[maxi] + 1)
                    ratio_r[maxi] += 1
                ratio = ratio_r.copy()
            result = list(map(change, range(N)))
            ans += int(min(result))

    print('#{} {}' .format(tc, ans))