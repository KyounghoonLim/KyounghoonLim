def my_max(arr):
    maxi = arr[0]
    for t in arr:
        if t > maxi:
            maxi = t

    return maxi


def is_increasing_num(n):
    if not n % 10:
        return
    while n % 10:
        a = n % 10
        n //= 10
        b = n % 10
        n //= 10
        if b <= a:
            continue
        else:
            return
    return True


def matching(idx=0, p_idx=1):
    if is_increasing_num(test_case[idx] * test_case[p_idx]):
        ans.append(test_case[idx] * test_case[p_idx])
    if p_idx < N - 1:
        matching(idx, p_idx + 1)
    else:
        if idx == N - 2:
            return
        matching(idx + 1, idx + 2)


T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    test_case = list(map(int, input().strip().split()))
    ans = []
    matching()
    if ans:
        print('#{} {}'.format(tc, my_max(ans)))
    else:
        print('#{} -1' .format(tc))