def is_in(n):
    for t_i in range(8):
        for t_j in range(len(dial[t_i])):
            if dial[t_i][t_j] == n:
                return t_i
    return 0


dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
        ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

test_case = input().strip()
ans = 0
for text in test_case:
    ans += is_in(text) + 3

print(ans)