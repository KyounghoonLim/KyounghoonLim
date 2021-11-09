def slicer(n):
    


x, y = map(int, input().strip().split())
N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]

paper_i = [0, y]
paper_j = [0, x]

for cut in test_case:
    if cut[0]:
