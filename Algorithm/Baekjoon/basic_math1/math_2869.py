A, B, V = map(int, input().strip().split())

ans = 1
V -= A
ans += V // (A - B)
if V % (A - B):
    ans += 1

print(ans)